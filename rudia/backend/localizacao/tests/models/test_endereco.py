from django.db import IntegrityError, transaction
from django.test import TestCase

from localizacao.models import Endereco


class EnderecoModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.endereco_base = Endereco.objects.create(
			cep='12345678',
			logradouro='Rua B',
			numero='01',
			complemento='Ap 10'
		)

	def test_should_retornar_string_quando_convertido(self):
		# Arrange
		endereco = self.endereco_base

		# Act
		result = str(endereco)

		# Assert
		self.assertEqual(result, 'Rua B, 01 - 12345678')

	def test_should_exigir_logradouro_numero_unico_quando_duplicado(self):
		# Arrange
		data = {
			'cep': '87654321',
			'logradouro': 'Rua B',
			'numero': '01',
		}

		# Act + Assert
		with transaction.atomic():
			with self.assertRaises(IntegrityError):
				Endereco.objects.create(**data)

	def test_should_permitir_mesmo_logradouro_com_numero_diferente(self):
		# Arrange
		data = {
			'cep': '99999999',
			'logradouro': 'Rua B',
			'numero': '02',
		}

		# Act
		endereco = Endereco.objects.create(**data)

		# Assert
		self.assertIsNotNone(endereco.id)

	def test_should_ordenar_por_logradouro_numero_quando_listado(self):
		# Arrange
		endereco_a2 = Endereco.objects.create(
			cep='11111111',
			logradouro='Rua A',
			numero='02'
		)
		endereco_a1 = Endereco.objects.create(
			cep='22222222',
			logradouro='Rua A',
			numero='01'
		)

		# Act
		ordered = list(Endereco.objects.all())

		# Assert
		self.assertEqual(ordered[0], endereco_a1)
		self.assertEqual(ordered[1], endereco_a2)
		self.assertEqual(ordered[2], self.endereco_base)
