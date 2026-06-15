from django.test import TestCase

from localizacao.models import Endereco
from localizacao.serializers import EnderecoResumoSerializer, EnderecoSerializer


class EnderecoSerializerTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.endereco = Endereco.objects.create(
			cep='12345678',
			logradouro='Rua A',
			numero='10',
			complemento='Ap 1'
		)

	def test_should_formatar_endereco_completo_quando_serializado(self):
		# Arrange
		serializer = EnderecoSerializer(self.endereco)

		# Act
		data = serializer.data

		# Assert
		self.assertEqual(data['endereco_completo'], 'Rua A, 10 - Ap 1 - CEP: 12345-678')

	def test_should_formatar_endereco_completo_sem_complemento(self):
		# Arrange
		endereco = Endereco.objects.create(
			cep='87654321',
			logradouro='Rua B',
			numero='20'
		)
		serializer = EnderecoSerializer(endereco)

		# Act
		data = serializer.data

		# Assert
		self.assertEqual(data['endereco_completo'], 'Rua B, 20 - CEP: 87654-321')

	def test_should_normalizar_cep_quando_validando(self):
		# Arrange
		serializer = EnderecoSerializer()

		# Act
		cep_normalizado = serializer.validate_cep('12.345-678')

		# Assert
		self.assertEqual(cep_normalizado, '12345678')

	def test_should_rejeitar_tamanho_cep_invalido(self):
		# Arrange
		serializer = EnderecoSerializer(data={
			'cep': '1234',
			'logradouro': 'Rua D',
			'numero': '40',
		})

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('cep', serializer.errors)

	def test_should_aceitar_numero_sn_quando_validando(self):
		# Arrange
		serializer = EnderecoSerializer(data={
			'cep': '11111111',
			'logradouro': 'Rua E',
			'numero': 's/n',
		})

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)
		self.assertEqual(serializer.validated_data['numero'], 'S/N')

	def test_should_rejeitar_numero_sem_digitos_ou_sn(self):
		# Arrange
		serializer = EnderecoSerializer(data={
			'cep': '22222222',
			'logradouro': 'Rua F',
			'numero': 'ABC',
		})

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('numero', serializer.errors)

	def test_should_normalizar_logradouro_quando_validando(self):
		# Arrange
		serializer = EnderecoSerializer(data={
			'cep': '33333333',
			'logradouro': '  rua g  ',
			'numero': '50',
		})

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)
		self.assertEqual(serializer.validated_data['logradouro'], 'Rua G')

	def test_should_rejeitar_logradouro_numero_duplicado_quando_criando(self):
		# Arrange
		serializer = EnderecoSerializer(data={
			'cep': '44444444',
			'logradouro': 'Rua A',
			'numero': '10',
		})

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertTrue(
			'endereco' in serializer.errors or 'non_field_errors' in serializer.errors
		)

	def test_should_ignorar_proprio_registro_quando_atualiza_mesmo_logradouro_numero(self):
		# Arrange
		serializer = EnderecoSerializer(
			self.endereco,
			data={'logradouro': 'Rua A', 'numero': '10'},
			partial=True
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)

	def test_should_ignorar_id_somente_leitura_quando_atualizacao_parcial(self):
		# Arrange
		serializer = EnderecoSerializer(self.endereco, data={'id': 999}, partial=True)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)
		self.assertNotIn('id', serializer.validated_data)

	def test_should_retornar_endereco_resumo_quando_serializado(self):
		# Arrange
		serializer = EnderecoResumoSerializer(self.endereco)

		# Act
		data = serializer.data

		# Assert
		self.assertEqual(data['endereco_completo'], 'Rua A, 10 - Ap 1')
