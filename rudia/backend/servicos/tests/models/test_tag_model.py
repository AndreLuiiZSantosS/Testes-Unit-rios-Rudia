from django.test import TestCase
from django.db import transaction
from django.db.utils import IntegrityError

from servicos.models import Categoria, Tag


class TagModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.categoria_passeios = Categoria.objects.create(nome='Passeios')
		cls.categoria_eventos = Categoria.objects.create(nome='Eventos')
		cls.tag_base = Tag.objects.create(
			nome='Aventura',
			descricao='Ao ar livre',
			categoria=cls.categoria_passeios
		)

	def test_should_retornar_string_quando_convertido(self):
		# Arrange
		tag = self.tag_base

		# Act
		result = str(tag)

		# Assert
		self.assertEqual(result, 'Tag: Aventura (Categoria: Passeios)')

	def test_should_exigir_nome_unico_quando_duplicado(self):
		# Arrange
		data = {
			'nome': 'Aventura',
			'descricao': 'Outra',
			'categoria': self.categoria_eventos
		}

		# Act + Assert
		with transaction.atomic():
			with self.assertRaises(IntegrityError):
				Tag.objects.create(**data)

	def test_should_exigir_nome_categoria_unico_quando_duplicado(self):
		# Arrange
		data = {
			'nome': 'Aventura',
			'descricao': 'Ao ar livre',
			'categoria': self.categoria_passeios
		}

		# Act + Assert
		with transaction.atomic():
			with self.assertRaises(IntegrityError):
				Tag.objects.create(**data)

	def test_should_ordenar_por_nome_e_categoria_quando_listado(self):
		# Arrange
		Tag.objects.create(
			nome='Cultura',
			descricao='Museus',
			categoria=self.categoria_eventos
		)
		Tag.objects.create(
			nome='Gastronomia',
			descricao='Teatro',
			categoria=self.categoria_passeios
		)

		# Act
		ordered = list(Tag.objects.all())

		# Assert
		self.assertEqual(
			[(tag.nome, tag.categoria.nome) for tag in ordered],
			sorted((tag.nome, tag.categoria.nome) for tag in ordered)
		)
