import shutil
import tempfile

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from rest_framework.test import APIRequestFactory

from localizacao.models import Cidade, Estado, ImagemCidade
from localizacao.serializers import (
	CidadeCreateUpdateSerializer,
	CidadeDetalheSerializer,
	CidadeListaSerializer,
	CidadeResumoSerializer,
)


class CidadeSerializerTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.estado_sp = Estado.objects.create(nome='Sao Paulo', sigla='SP')
		cls.estado_rj = Estado.objects.create(nome='Rio', sigla='RJ')
		cls.cidade_sp = Cidade.objects.create(nome='Campinas', estado=cls.estado_sp)

	def setUp(self):
		self._media_root = tempfile.mkdtemp()
		self._media_override = override_settings(MEDIA_ROOT=self._media_root)
		self._media_override.enable()
		self.addCleanup(self._media_override.disable)
		self.addCleanup(lambda: shutil.rmtree(self._media_root, ignore_errors=True))

	def _make_image_file(self, name='cidade.gif'):
		image_content = (
			b'GIF87a\x01\x00\x01\x00\x80\x01\x00\x00\x00\x00'
			b'\xff\xff\xff!\xf9\x04\x01\x00\x00\x00\x00,\x00'
			b'\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02D\x01\x00;'
		)
		return SimpleUploadedFile(name, image_content, content_type='image/gif')

	def test_should_normalizar_nome_quando_valido(self):
		# Arrange
		serializer = CidadeCreateUpdateSerializer(
			data={'nome': '  piracicaba  ', 'estado': self.estado_sp.id}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)
		self.assertEqual(serializer.validated_data['nome'], 'Piracicaba')

	def test_should_rejeitar_nome_duplicado_no_mesmo_estado_quando_criando(self):
		# Arrange
		serializer = CidadeCreateUpdateSerializer(
			data={'nome': 'Campinas', 'estado': self.estado_sp.id}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertTrue(
			'nome' in serializer.errors or 'non_field_errors' in serializer.errors
		)

	def test_should_permitir_nome_duplicado_em_estado_diferente(self):
		# Arrange
		serializer = CidadeCreateUpdateSerializer(
			data={'nome': 'Campinas', 'estado': self.estado_rj.id}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)

	def test_should_ignorar_proprio_registro_quando_atualiza_mesmo_nome_estado(self):
		# Arrange
		serializer = CidadeCreateUpdateSerializer(
			self.cidade_sp,
			data={'nome': 'Campinas', 'estado': self.estado_sp.id},
			partial=True
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)

	def test_should_ignorar_id_somente_leitura_quando_atualizacao_parcial(self):
		# Arrange
		serializer = CidadeCreateUpdateSerializer(
			self.cidade_sp,
			data={'id': 999},
			partial=True
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)
		self.assertNotIn('id', serializer.validated_data)

	def test_should_incluir_total_imagens_quando_serializado(self):
		# Arrange
		ImagemCidade.objects.create(
			cidade=self.cidade_sp,
			caminho_imagem=self._make_image_file('img1.gif')
		)
		ImagemCidade.objects.create(
			cidade=self.cidade_sp,
			caminho_imagem=self._make_image_file('img2.gif')
		)
		serializer = CidadeListaSerializer(self.cidade_sp)

		# Act
		data = serializer.data

		# Assert
		self.assertEqual(data['total_imagens'], 2)
		self.assertEqual(data['estado']['sigla'], 'SP')

	def test_should_incluir_imagens_com_urls_absolutas_quando_serializado(self):
		# Arrange
		imagem = ImagemCidade.objects.create(
			cidade=self.cidade_sp,
			caminho_imagem=self._make_image_file('img3.gif')
		)
		request = APIRequestFactory().get('/')
		serializer = CidadeDetalheSerializer(
			self.cidade_sp,
			context={'request': request}
		)

		# Act
		data = serializer.data

		# Assert
		self.assertEqual(data['total_imagens'], 1)
		self.assertEqual(data['imagens'][0]['id'], imagem.id)
		self.assertIn('http://testserver/', data['imagens'][0]['caminho_imagem'])

	def test_should_retornar_sigla_estado_quando_serializado(self):
		# Arrange
		serializer = CidadeResumoSerializer(self.cidade_sp)

		# Act
		data = serializer.data

		# Assert
		self.assertEqual(data['estado_sigla'], 'SP')
