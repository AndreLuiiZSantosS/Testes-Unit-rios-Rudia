from django.db import IntegrityError, transaction
from django.test import TestCase

from localizacao.models import Estado


class EstadoModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.estado_sp = Estado.objects.create(nome='Sao Paulo', sigla='SP')
		cls.estado_rj = Estado.objects.create(nome='Rio', sigla='RJ')

	def test_should_retornar_string_quando_convertido(self):
		# Arrange
		estado = self.estado_sp

		# Act
		result = str(estado)

		# Assert
		self.assertEqual(result, 'Sao Paulo (SP)')

	def test_should_exigir_nome_unico_quando_duplicado(self):
		# Arrange
		data = {'nome': 'Sao Paulo', 'sigla': 'XX'}

		# Act + Assert
		with transaction.atomic():
			with self.assertRaises(IntegrityError):
				Estado.objects.create(**data)

	def test_should_exigir_sigla_unica_quando_duplicada(self):
		# Arrange
		data = {'nome': 'Paraiba', 'sigla': 'SP'}

		# Act + Assert
		with transaction.atomic():
			with self.assertRaises(IntegrityError):
				Estado.objects.create(**data)

	def test_should_ordenar_por_nome_quando_listado(self):
		# Arrange
		Estado.objects.create(nome='Amazonas', sigla='AM')

		# Act
		ordered = list(Estado.objects.all())

		# Assert
		self.assertEqual([estado.nome for estado in ordered], ['Amazonas', 'Rio', 'Sao Paulo'])
