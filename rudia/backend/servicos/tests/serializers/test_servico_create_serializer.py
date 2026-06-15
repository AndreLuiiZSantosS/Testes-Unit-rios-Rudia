import base64
from types import SimpleNamespace

from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework.test import APIRequestFactory

from servicos.models import Categoria, Tag, HorarioFuncionamento, Servico
from servicos.serializers.servico_create import ServicoCreateSerializer
from localizacao.models import Estado, Cidade, Endereco
from moderacao.models import Proposta
from usuarios.models import Parceiro


class ServicoCreateSerializerTest(TestCase):
	@staticmethod
	def _make_base64_image():
		image_content = (
			b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00'
			b'\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00'
			b'\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
		)
		encoded = base64.b64encode(image_content).decode('ascii')
		return f'data:image/gif;base64,{encoded}'

	@classmethod
	def setUpTestData(cls):
		cls.estado_sp = Estado.objects.create(nome='Sao Paulo', sigla='SP')
		cls.cidade_sp = Cidade.objects.create(nome='Campinas', estado=cls.estado_sp)
		cls.categoria_passeios = Categoria.objects.create(nome='Passeios')
		cls.categoria_eventos = Categoria.objects.create(nome='Eventos')
		cls.tag_valida = Tag.objects.create(
			nome='Aventura',
			descricao='Ao ar livre',
			categoria=cls.categoria_passeios
		)
		cls.tag_invalida = Tag.objects.create(
			nome='Gastronomia',
			descricao='Culinaria local',
			categoria=cls.categoria_eventos
		)
		cls.parceiro = Parceiro.objects.create_user(
			username='parceiro1',
			email='parceiro1@test.com',
			password='12345678',
			nome='Parceiro Um',
			cnpj='12345678901234'
		)
		cls.factory = APIRequestFactory()

	def _make_request(self):
		request = self.factory.post('/api/servicos/', {})
		request.user = SimpleNamespace(parceiro=self.parceiro)
		return request

	def _make_payload(self):
		return {
			'nome': 'Passeio de Barco',
			'descricao': 'Passeio com guia local',
			'capacidade_maxima': 10,
			'preco_minimo': '100.00',
			'preco_maximo': '200.00',
			'imagem_capa': self._make_base64_image(),
			'categoria': self.categoria_passeios.id,
			'cidade': self.cidade_sp.id,
			'tags': [self.tag_valida.id],
			'endereco': {
				'cep': '12345678',
				'logradouro': 'Rua A',
				'numero': '100'
			},
			'horarios_funcionamento': [
				{
					'dia_semana': HorarioFuncionamento.DiaSemana.SEGUNDA,
					'hora_abertura': '08:00',
					'hora_fechamento': '17:00'
				},
				{
					'dia_semana': HorarioFuncionamento.DiaSemana.SABADO,
					'hora_abertura': '09:00',
					'hora_fechamento': '13:00'
				}
			]
		}

	def test_should_ser_valido_quando_payload_ok(self):
		# Arrange
		payload = self._make_payload()

		# Act
		serializer = ServicoCreateSerializer(data=payload, context={'request': self._make_request()})
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)

	def test_should_rejeitar_quando_preco_maximo_menor(self):
		# Arrange
		payload = self._make_payload()
		payload['preco_minimo'] = '200.00'
		payload['preco_maximo'] = '150.00'

		# Act
		serializer = ServicoCreateSerializer(data=payload, context={'request': self._make_request()})
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('preco_maximo', serializer.errors)

	def test_should_rejeitar_quando_capacidade_maxima_invalida(self):
		# Arrange
		payload = self._make_payload()
		payload['capacidade_maxima'] = 0

		# Act
		serializer = ServicoCreateSerializer(data=payload, context={'request': self._make_request()})
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('capacidade_maxima', serializer.errors)

	def test_should_rejeitar_quando_tag_nao_pertence_categoria(self):
		# Arrange
		payload = self._make_payload()
		payload['tags'] = [self.tag_invalida.id]

		# Act
		serializer = ServicoCreateSerializer(data=payload, context={'request': self._make_request()})
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('tags', serializer.errors)

	def test_should_rejeitar_quando_dia_semana_duplicado(self):
		# Arrange
		payload = self._make_payload()
		payload['horarios_funcionamento'] = [
			{
				'dia_semana': HorarioFuncionamento.DiaSemana.SEGUNDA,
				'hora_abertura': '08:00',
				'hora_fechamento': '17:00'
			},
			{
				'dia_semana': HorarioFuncionamento.DiaSemana.SEGUNDA,
				'hora_abertura': '09:00',
				'hora_fechamento': '18:00'
			}
		]

		# Act
		serializer = ServicoCreateSerializer(data=payload, context={'request': self._make_request()})
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('horarios_funcionamento', serializer.errors)

	def test_should_criar_servico_endereco_horarios_e_proposta_quando_salva(self):
		# Arrange
		payload = self._make_payload()
		serializer = ServicoCreateSerializer(
			data=payload,
			context={'request': self._make_request()}
		)
		serializer.is_valid(raise_exception=True)

		# Act
		servico = serializer.save()

		# Assert
		self.assertIsNotNone(servico.id)
		self.assertFalse(servico.ativo)
		self.assertEqual(servico.parceiro, self.parceiro)
		self.assertEqual(servico.endereco.logradouro, 'Rua A')
		self.assertEqual(servico.tags.count(), 1)
		self.assertEqual(servico.horarios_funcionamento.count(), 2)
		self.assertTrue(
			Proposta.objects.filter(object_id=servico.id).exists()
		)

	def test_should_ignorar_id_somente_leitura_quando_atualizacao_parcial(self):
		# Arrange
		endereco = Endereco.objects.create(cep='99999999', logradouro='Rua Z', numero='9')
		image_content = (
			b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00'
			b'\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00'
			b'\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
		)
		servico = Servico.objects.create(
			nome='Tour Historico',
			descricao='Centro antigo',
			capacidade_maxima=5,
			preco_minimo='80.00',
			preco_maximo='120.00',
			imagem_capa=SimpleUploadedFile(
				'servico.gif',
				image_content,
				content_type='image/gif'
			),
			parceiro=self.parceiro,
			categoria=self.categoria_passeios,
			cidade=self.cidade_sp,
			endereco=endereco
		)

		# Act
		serializer = ServicoCreateSerializer(
			servico,
			data={'id': 999},
			partial=True,
			context={'request': self._make_request()}
		)
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)
		self.assertNotIn('id', serializer.validated_data)
