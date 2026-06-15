from django.db import IntegrityError, transaction
from django.test import TestCase

from localizacao.models import Cidade, Estado


class CidadeModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.estado_sp = Estado.objects.create(nome='Sao Paulo', sigla='SP')
		cls.estado_rj = Estado.objects.create(nome='Rio', sigla='RJ')
		cls.cidade_sp = Cidade.objects.create(nome='Alpha', estado=cls.estado_sp)

	def test_should_retornar_string_quando_convertido(self):
		# Arrange
		cidade = self.cidade_sp

		# Act
		result = str(cidade)

		# Assert
		self.assertEqual(result, 'Alpha - SP')

	def test_should_exigir_nome_estado_unico_quando_duplicado(self):
		# Arrange
		data = {'nome': 'Alpha', 'estado': self.estado_sp}

		# Act + Assert
		with transaction.atomic():
			with self.assertRaises(IntegrityError):
				Cidade.objects.create(**data)

	def test_should_permitir_mesmo_nome_em_estado_diferente(self):
		# Arrange
		data = {'nome': 'Alpha', 'estado': self.estado_rj}

		# Act
		cidade = Cidade.objects.create(**data)

		# Assert
		self.assertIsNotNone(cidade.id)

	def test_should_ordenar_por_nome_e_sigla_estado_quando_listado(self):
		# Arrange
		cidade_rj = Cidade.objects.create(nome='Alpha', estado=self.estado_rj)
		cidade_beta = Cidade.objects.create(nome='Beta', estado=self.estado_sp)

		# Act
		ordered = list(Cidade.objects.all())

		# Assert
		self.assertEqual(ordered[0], cidade_rj)
		self.assertEqual(ordered[1], self.cidade_sp)
		self.assertEqual(ordered[2], cidade_beta)
