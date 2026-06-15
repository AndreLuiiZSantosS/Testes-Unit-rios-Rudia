from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from servicos.models import Categoria, Servico, HorarioFuncionamento
from servicos.serializers.horario_funcionamento import HorarioFuncionamentoSerializer
from localizacao.models import Estado, Cidade, Endereco
from usuarios.models import Parceiro


class HorarioFuncionamentoSerializerTest(TestCase):
	@staticmethod
	def _make_image_file(name='servico.gif'):
		image_content = (
			b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00'
			b'\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00'
			b'\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
		)
		return SimpleUploadedFile(name, image_content, content_type='image/gif')

	@classmethod
	def setUpTestData(cls):
		estado = Estado.objects.create(nome='Sao Paulo', sigla='SP')
		cidade = Cidade.objects.create(nome='Campinas', estado=estado)
		categoria = Categoria.objects.create(nome='Passeios')
		parceiro = Parceiro.objects.create_user(
			username='parceiro1',
			email='parceiro1@test.com',
			password='12345678',
			nome='Parceiro Um',
			cnpj='12345678901234'
		)
		endereco = Endereco.objects.create(
			cep='12345678',
			logradouro='Rua A',
			numero='100'
		)
		cls.servico = Servico.objects.create(
			nome='Passeio de Barco',
			descricao='Passeio com guia local',
			capacidade_maxima=10,
			preco_minimo='100.00',
			preco_maximo='200.00',
			imagem_capa=cls._make_image_file(),
			parceiro=parceiro,
			categoria=categoria,
			cidade=cidade,
			endereco=endereco
		)
		cls.horario = HorarioFuncionamento.objects.create(
			hora_abertura='08:00',
			hora_fechamento='17:00',
			dia_semana=HorarioFuncionamento.DiaSemana.SEGUNDA,
			servico=cls.servico
		)

	def test_should_ser_valido_quando_payload_ok(self):
		# Arrange
		payload = {
			'dia_semana': HorarioFuncionamento.DiaSemana.QUARTA,
			'hora_abertura': '09:00',
			'hora_fechamento': '18:00'
		}

		# Act
		serializer = HorarioFuncionamentoSerializer(data=payload)
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)

	def test_should_rejeitar_quando_hora_fechamento_igual_ou_menor(self):
		# Arrange
		payload = {
			'dia_semana': HorarioFuncionamento.DiaSemana.SEGUNDA,
			'hora_abertura': '10:00',
			'hora_fechamento': '10:00'
		}

		# Act
		serializer = HorarioFuncionamentoSerializer(data=payload)
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('non_field_errors', serializer.errors)

	def test_should_incluir_dia_semana_display_quando_serializado(self):
		# Arrange
		serializer = HorarioFuncionamentoSerializer(self.horario)

		# Act
		data = serializer.data

		# Assert
		self.assertEqual(data['dia_semana_display'], self.horario.get_dia_semana_display())

	def test_should_ignorar_id_somente_leitura_quando_atualizacao_parcial(self):
		# Arrange
		serializer = HorarioFuncionamentoSerializer(
			self.horario,
			data={'id': 999, 'hora_abertura': '07:00'},
			partial=True
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)
		self.assertNotIn('id', serializer.validated_data)
