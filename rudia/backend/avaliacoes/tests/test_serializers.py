from decimal import Decimal
from django.test import TestCase
from django.contrib.contenttypes.models import ContentType
from rest_framework.exceptions import ErrorDetail

from avaliacoes.models import Avaliacao
from avaliacoes.serializers.avaliacao import (
	AvaliacaoSerializer,
	AvaliacaoCreateSerializer,
	AvaliacaoResumoSerializer,
	AvaliacaoPreviewSerializer,
)
from usuarios.models import Rudiero
from localizacao.models import Estado


class AvaliacaoSerializerTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.rudiero = Rudiero.objects.create(
			username='rudi2',
			email='rudi2@example.com',
			nome='Rudi Two',
			data_nascimento='1991-02-02',
			genero='M'
		)

		cls.estado = Estado.objects.create(nome='Sao Paulo', sigla='SP')
		cls.content_type = ContentType.objects.get_for_model(Estado)

		cls.av = Avaliacao.objects.create(
			nota=Decimal('4.0'),
			comentario='Legal',
			rudiero=cls.rudiero,
			content_type=cls.content_type,
			object_id=cls.estado.id,
		)

	def test_should_incluir_campos_esperados_e_tipo_objeto_quando_serializado(self):
		# Arrange
		serializer = AvaliacaoSerializer(self.av)

		# Act
		data = serializer.data

		# Assert
		self.assertEqual(data['tipo_objeto'], 'estado')
		self.assertIn('rudiero', data)
		self.assertEqual(data['rudiero']['username'], self.rudiero.username)
		self.assertEqual(data['objeto_avaliado']['id'], self.estado.id)

	def test_should_rejeitar_nota_invalida_e_objeto_inexistente_quando_criando(self):
		# Arrange: invalid nota
		valid_ct = self.content_type.id
		serializer_invalid_nota = AvaliacaoCreateSerializer(data={
			'nota': Decimal('6.0'),
			'comentario': 'X',
			'content_type': valid_ct,
			'object_id': self.estado.id,
		})

		# Act + Assert
		self.assertFalse(serializer_invalid_nota.is_valid())
		self.assertIn('nota', serializer_invalid_nota.errors)

		# Arrange: non-existent object
		serializer_invalid_obj = AvaliacaoCreateSerializer(data={
			'nota': Decimal('4.0'),
			'comentario': 'X',
			'content_type': valid_ct,
			'object_id': 999999,
		})

		# Act + Assert
		self.assertFalse(serializer_invalid_obj.is_valid())
		self.assertIn('object_id', serializer_invalid_obj.errors)

		# Arrange: valid payload
		serializer_valid = AvaliacaoCreateSerializer(data={
			'nota': Decimal('3.5'),
			'comentario': 'Ok',
			'content_type': valid_ct,
			'object_id': self.estado.id,
		})

		# Act + Assert
		self.assertTrue(serializer_valid.is_valid())

	def test_should_serializar_resumo_e_preview_quando_gerado(self):
		# Resumo
		resumo = AvaliacaoResumoSerializer(self.av)
		data_resumo = resumo.data
		self.assertEqual(data_resumo['rudiero_username'], self.rudiero.username)

		# Preview without request returns None for foto
		preview = AvaliacaoPreviewSerializer(self.av)
		data_preview = preview.data
		self.assertIsNone(data_preview.get('rudiero_foto'))

