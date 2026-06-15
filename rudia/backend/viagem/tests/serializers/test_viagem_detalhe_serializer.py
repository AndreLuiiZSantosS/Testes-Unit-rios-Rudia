import shutil
import tempfile
from decimal import Decimal

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from rest_framework.test import APIRequestFactory

from localizacao.models import Cidade, Endereco, Estado
from servicos.models import Categoria, Servico
from usuarios.models import Parceiro, Rudiero
from viagem.models import Viagem
from viagem.serializers import ViagemDetalheSerializer


class ViagemDetalheSerializerTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.estado = Estado.objects.create(nome='Sao Paulo', sigla='SP')
		cls.cidade = Cidade.objects.create(nome='Campinas', estado=cls.estado)

		cls.categoria_hospedagem = Categoria.objects.create(nome='Hospedagem')
		cls.categoria_transporte = Categoria.objects.create(nome='Transporte')
		cls.categoria_alimentacao = Categoria.objects.create(nome='Alimentação')
		cls.categoria_lazer = Categoria.objects.create(nome='Lazer')

		cls.parceiro = Parceiro.objects.create_user(
			username='parceiro1',
			email='parceiro1@example.com',
			nome='Parceiro 1',
			password='senha123',
			cnpj='12345678000199'
		)
		cls.rudiero = Rudiero.objects.create_user(
			username='rudiero1',
			email='rudiero1@example.com',
			nome='Rudiero 1',
			password='senha123',
			data_nascimento='1990-01-01'
		)

		cls.viagem = Viagem.objects.create(
			nome='Viagem Detalhe',
			descricao='Descricao detalhada',
			dias=3,
			orcamento_total=Decimal('900.00'),
			viajantes_adultos=2,
			viajantes_criancas=1,
			rudiero=cls.rudiero,
			cidade_destino=cls.cidade,
		)

	def setUp(self):
		self._media_root = tempfile.mkdtemp()
		self._media_override = override_settings(MEDIA_ROOT=self._media_root)
		self._media_override.enable()
		self.addCleanup(self._media_override.disable)
		self.addCleanup(lambda: shutil.rmtree(self._media_root, ignore_errors=True))
		self._endereco_seq = 0

	def _make_image_file(self, name='capa.gif'):
		image_content = (
			b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00'
			b'\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00'
			b'\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
		)
		return SimpleUploadedFile(name, image_content, content_type='image/gif')

	def _create_servico(self, nome, categoria):
		self._endereco_seq += 1
		endereco = Endereco.objects.create(
			cep='12345678',
			logradouro='Rua Teste',
			numero=str(100 + self._endereco_seq)
		)
		return Servico.objects.create(
			nome=nome,
			descricao='Descricao',
			capacidade_maxima=10,
			preco_minimo=Decimal('100.00'),
			preco_maximo=Decimal('200.00'),
			ativo=True,
			imagem_capa=self._make_image_file(f'{nome}.gif'),
			parceiro=self.parceiro,
			categoria=categoria,
			cidade=self.cidade,
			endereco=endereco,
		)

	def _build_request(self):
		return APIRequestFactory().get('/')

	def test_should_calcular_total_viajantes_quando_serializado(self):
		# Arrange
		serializer = ViagemDetalheSerializer(
			self.viagem,
			context={'request': self._build_request()}
		)

		# Act
		data = serializer.data

		# Assert
		self.assertEqual(data['total_viajantes'], 3)

	def test_should_agrupar_servicos_por_categoria_quando_serializado(self):
		# Arrange
		hospedagem = self._create_servico('Hotel', self.categoria_hospedagem)
		transporte = self._create_servico('Transporte', self.categoria_transporte)
		alimentacao_a = self._create_servico('Restaurante A', self.categoria_alimentacao)
		alimentacao_b = self._create_servico('Restaurante B', self.categoria_alimentacao)
		lazer_a = self._create_servico('Parque', self.categoria_lazer)
		lazer_b = self._create_servico('Museu', self.categoria_lazer)
		self.viagem.servicos.set([
			hospedagem,
			transporte,
			alimentacao_a,
			alimentacao_b,
			lazer_a,
			lazer_b,
		])
		serializer = ViagemDetalheSerializer(
			self.viagem,
			context={'request': self._build_request()}
		)

		# Act
		data = serializer.data
		servicos = data['servicos']

		# Assert
		self.assertEqual(servicos['hospedagem']['id'], hospedagem.id)
		self.assertEqual(servicos['transporte']['id'], transporte.id)
		self.assertEqual(len(servicos['alimentacao']), 2)
		self.assertEqual(len(servicos['lazer']), 2)
		self.assertEqual(servicos['alimentacao'][0]['categoria'], 'Alimentação')
		self.assertTrue(servicos['hospedagem']['imagem_capa_url'].startswith('http://testserver/'))

	def test_should_incluir_resumos_quando_serializado(self):
		# Arrange
		serializer = ViagemDetalheSerializer(
			self.viagem,
			context={'request': self._build_request()}
		)

		# Act
		data = serializer.data

		# Assert
		self.assertEqual(data['rudiero']['id'], self.rudiero.id)
		self.assertEqual(data['rudiero']['username'], self.rudiero.username)
		self.assertEqual(data['cidade_destino']['id'], self.cidade.id)
		self.assertEqual(data['cidade_destino']['estado_sigla'], 'SP')
