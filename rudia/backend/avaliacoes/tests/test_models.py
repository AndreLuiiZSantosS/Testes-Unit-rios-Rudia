from decimal import Decimal
from django.db import IntegrityError, transaction
from django.test import TestCase
from django.contrib.contenttypes.models import ContentType

from avaliacoes.models import Avaliacao
from usuarios.models import Rudiero
from localizacao.models import Estado


class AvaliacaoModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.rudiero = Rudiero.objects.create(
			username='rudi',
			email='rudi@example.com',
			nome='Rudi Test',
			data_nascimento='1990-01-01',
			genero='M'
		)

		cls.estado = Estado.objects.create(nome='Sao Paulo', sigla='SP')

		cls.content_type = ContentType.objects.get_for_model(Estado)

		cls.av1 = Avaliacao.objects.create(
			nota=Decimal('4.5'),
			comentario='Muito bom',
			rudiero=cls.rudiero,
			content_type=cls.content_type,
			object_id=cls.estado.id
		)

	def test_should_retornar_string_quando_convertido(self):
		# Arrange
		aval = self.av1

		# Act
		result = str(aval)

		# Assert
		self.assertIn('Avaliação de', result)
		self.assertIn('4.5', result)

	def test_should_exigir_unicidade_por_rudiero_e_objeto_quando_duplicado(self):
		# Arrange
		data = {
			'nota': Decimal('3.0'),
			'comentario': 'Outra',
			'rudiero': self.rudiero,
			'content_type': self.content_type,
			'object_id': self.estado.id,
		}

		# Act + Assert
		with transaction.atomic():
			with self.assertRaises(IntegrityError):
				Avaliacao.objects.create(**data)

	def test_should_ordenar_por_data_avaliacao_desc_quando_listado(self):
		# Arrange
		a_old = self.av1
		a_new = Avaliacao.objects.create(
			nota=Decimal('5.0'),
			comentario='Recente',
			rudiero=self.rudiero,
			content_type=self.content_type,
			object_id=self.estado.id + 1  # different object_id so uniqueness does not block
		)

		# Act
		ordered = list(Avaliacao.objects.all())

		# Assert: newest first
		self.assertEqual(ordered[0], a_new)
		self.assertEqual(ordered[1], a_old)

