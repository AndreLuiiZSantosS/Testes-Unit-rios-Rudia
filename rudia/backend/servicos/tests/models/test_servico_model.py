from django.test import TestCase
from django.db import transaction
from django.db.utils import IntegrityError
from django.core.files.uploadedfile import SimpleUploadedFile

from servicos.models import Servico, Categoria, Tag
from localizacao.models import Estado, Cidade, Endereco
from usuarios.models import Parceiro


class ServicoModelTest(TestCase):
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
		cls.estado_sp = Estado.objects.create(nome='Sao Paulo', sigla='SP')
		cls.cidade_sp = Cidade.objects.create(nome='Campinas', estado=cls.estado_sp)
		cls.categoria = Categoria.objects.create(nome='Passeios')
		cls.tag = Tag.objects.create(nome='Aventura', descricao='Ao ar livre', categoria=cls.categoria)

		cls.parceiro_um = Parceiro.objects.create_user(
			username='parceiro1',
			email='parceiro1@test.com',
			password='12345678',
			nome='Parceiro Um',
			cnpj='12345678901234'
		)
		cls.parceiro_dois = Parceiro.objects.create_user(
			username='parceiro2',
			email='parceiro2@test.com',
			password='12345678',
			nome='Parceiro Dois',
			cnpj='98765432109876'
		)

		cls.endereco_base = Endereco.objects.create(
			cep='12345678',
			logradouro='Rua A',
			numero='100'
		)
		cls.servico_base = Servico.objects.create(
			nome='Passeio de Barco',
			descricao='Passeio com guia local',
			capacidade_maxima=10,
			preco_minimo='100.00',
			preco_maximo='200.00',
			imagem_capa=cls._make_image_file(),
			parceiro=cls.parceiro_um,
			categoria=cls.categoria,
			cidade=cls.cidade_sp,
			endereco=cls.endereco_base
		)
		cls.servico_base.tags.set([cls.tag])

	def test_should_retornar_string_quando_convertido(self):
		# Arrange
		servico = self.servico_base

		# Act
		result = str(servico)

		# Assert
		self.assertEqual(result, 'Passeio de Barco - @parceiro1 - Ativo: NÃO')

	def test_should_definir_ativo_como_false_quando_criado(self):
		# Arrange
		servico = self.servico_base

		# Act
		ativo = servico.ativo

		# Assert
		self.assertFalse(ativo)

	def test_should_exigir_nome_parceiro_unico_quando_duplicado(self):
		# Arrange
		endereco = Endereco.objects.create(
			cep='87654321',
			logradouro='Rua B',
			numero='200'
		)
		data = {
			'nome': 'Passeio de Barco',
			'descricao': 'Passeio com guia local',
			'capacidade_maxima': 8,
			'preco_minimo': '80.00',
			'preco_maximo': '160.00',
			'imagem_capa': self._make_image_file('servico2.gif'),
			'parceiro': self.parceiro_um,
			'categoria': self.categoria,
			'cidade': self.cidade_sp,
			'endereco': endereco
		}

		# Act + Assert
		with transaction.atomic():
			with self.assertRaises(IntegrityError):
				Servico.objects.create(**data)

	def test_should_permitir_mesmo_nome_para_parceiro_diferente(self):
		# Arrange
		endereco = Endereco.objects.create(
			cep='33333333',
			logradouro='Rua C',
			numero='300'
		)
		data = {
			'nome': 'Passeio de Barco',
			'descricao': 'Passeio com guia local',
			'capacidade_maxima': 12,
			'preco_minimo': '120.00',
			'preco_maximo': '220.00',
			'imagem_capa': self._make_image_file('servico3.gif'),
			'parceiro': self.parceiro_dois,
			'categoria': self.categoria,
			'cidade': self.cidade_sp,
			'endereco': endereco
		}

		# Act
		servico = Servico.objects.create(**data)

		# Assert
		self.assertIsNotNone(servico.id)

	def test_should_ordenar_por_nome_quando_listado(self):
		# Arrange
		endereco_a = Endereco.objects.create(
			cep='44444444',
			logradouro='Rua D',
			numero='400'
		)
		endereco_z = Endereco.objects.create(
			cep='55555555',
			logradouro='Rua E',
			numero='500'
		)
		Servico.objects.create(
			nome='Aventura na Serra',
			descricao='Trilha guiada',
			capacidade_maxima=6,
			preco_minimo='90.00',
			preco_maximo='140.00',
			imagem_capa=self._make_image_file('servico4.gif'),
			parceiro=self.parceiro_um,
			categoria=self.categoria,
			cidade=self.cidade_sp,
			endereco=endereco_a
		)
		Servico.objects.create(
			nome='Zoologico Noturno',
			descricao='Visita noturna guiada',
			capacidade_maxima=20,
			preco_minimo='70.00',
			preco_maximo='120.00',
			imagem_capa=self._make_image_file('servico5.gif'),
			parceiro=self.parceiro_um,
			categoria=self.categoria,
			cidade=self.cidade_sp,
			endereco=endereco_z
		)

		# Act
		ordered = list(Servico.objects.all())

		# Assert
		self.assertEqual(
			[servico.nome for servico in ordered],
			sorted([servico.nome for servico in ordered])
		)
