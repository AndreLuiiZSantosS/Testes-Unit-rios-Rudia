from django.test import TestCase
from django.db import transaction
from django.db.utils import IntegrityError

from servicos.models import Categoria


class CategoriaModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.categoria_base = Categoria.objects.create(nome='Passeios')

	def test_should_retornar_string_quando_convertido(self):
		# Arrange
		categoria = self.categoria_base

		# Act
		result = str(categoria)

		# Assert
		self.assertEqual(result, 'Passeios')

	def test_should_exigir_nome_unico_quando_duplicado(self):
		# Arrange
		data = {'nome': 'Passeios'}

		# Act + Assert
		with transaction.atomic():
			with self.assertRaises(IntegrityError):
				Categoria.objects.create(**data)

	def test_should_ordenar_por_nome_quando_listado(self):
		# Arrange
		Categoria.objects.create(nome='Aventura')
		Categoria.objects.create(nome='Zoologico')

		# Act
		ordered = list(Categoria.objects.all())

		# Assert
		self.assertEqual(
			[categoria.nome for categoria in ordered],
			sorted([categoria.nome for categoria in ordered])
		)
