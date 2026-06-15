from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.contenttypes.models import ContentType
from rest_framework.test import APIRequestFactory

from avaliacoes.models import Avaliacao
from servicos.models import Categoria, Tag, HorarioFuncionamento, Servico
from servicos.serializers.servico_detalhe import ServicoDetalheSerializer
from localizacao.models import Estado, Cidade, Endereco
from usuarios.models import Parceiro, Rudiero


class ServicoDetalheSerializerTest(TestCase):
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
		cls.tag = Tag.objects.create(
			nome='Aventura',
			descricao='Ao ar livre',
			categoria=cls.categoria
		)
		cls.parceiro = Parceiro.objects.create_user(
			username='parceiro1',
			email='parceiro1@test.com',
			password='12345678',
			nome='Parceiro Um',
			cnpj='12345678901234'
		)
		cls.endereco = Endereco.objects.create(
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
			parceiro=cls.parceiro,
			categoria=cls.categoria,
			cidade=cls.cidade_sp,
			endereco=cls.endereco
		)
		cls.servico.tags.set([cls.tag])
		cls.factory = APIRequestFactory()

	def _make_serializer(self, request=None):
		context = {'request': request} if request else {}
		return ServicoDetalheSerializer(self.servico, context=context)

	def _create_avaliacao(self, nota):
		rudiero = Rudiero.objects.create_user(
			username=f'rudiero{nota}'.replace('.', ''),
			email=f'rudiero{nota}@test.com'.replace('.', ''),
			password='12345678',
			nome='Rudiero Teste',
			data_nascimento='1990-01-01'
		)
		return Avaliacao.objects.create(
			nota=nota,
			comentario='Teste',
			rudiero=rudiero,
			content_type=ContentType.objects.get_for_model(Servico),
			object_id=self.servico.id
		)

	def test_should_calcular_preco_medio_quando_precos_presentes(self):
		# Arrange
		serializer = self._make_serializer()

		# Act
		preco_medio = serializer.get_preco_medio(self.servico)

		# Assert
		self.assertEqual(preco_medio, 150.0)

	def test_should_retornar_imagem_capa_url_quando_request(self):
		# Arrange
		request = self.factory.get('/')
		serializer = self._make_serializer(request=request)

		# Act
		url = serializer.get_imagem_capa_url(self.servico)

		# Assert
		self.assertIn('http://testserver/', url)
		self.assertIn('fotos_servico/', url)

	def test_should_ordenar_horarios_por_dia_semana(self):
		# Arrange
		HorarioFuncionamento.objects.create(
			hora_abertura='09:00',
			hora_fechamento='18:00',
			dia_semana=HorarioFuncionamento.DiaSemana.DOMINGO,
			servico=self.servico
		)
		HorarioFuncionamento.objects.create(
			hora_abertura='08:00',
			hora_fechamento='17:00',
			dia_semana=HorarioFuncionamento.DiaSemana.SEGUNDA,
			servico=self.servico
		)
		HorarioFuncionamento.objects.create(
			hora_abertura='10:00',
			hora_fechamento='19:00',
			dia_semana=HorarioFuncionamento.DiaSemana.TERCA,
			servico=self.servico
		)
		serializer = self._make_serializer()

		# Act
		data = serializer.get_horarios_funcionamento(self.servico)

		# Assert
		self.assertEqual([item['dia_semana'] for item in data], ['SEG', 'TER', 'DOM'])

	def test_should_retornar_avaliacoes_resumo_quando_calcula(self):
		# Arrange
		self._create_avaliacao(5.0)
		self._create_avaliacao(4.5)
		self._create_avaliacao(3.5)
		self._create_avaliacao(2.5)
		self._create_avaliacao(1.0)
		serializer = self._make_serializer()

		# Act
		resumo = serializer.get_avaliacoes_resumo(self.servico)

		# Assert
		self.assertEqual(resumo['media_geral'], 3.3)
		self.assertEqual(resumo['total'], 5)
		self.assertEqual(resumo['distribuicao']['cinco_estrelas'], 1)
		self.assertEqual(resumo['distribuicao']['quatro_estrelas'], 1)
		self.assertEqual(resumo['distribuicao']['tres_estrelas'], 1)
		self.assertEqual(resumo['distribuicao']['dois_estrelas'], 1)
		self.assertEqual(resumo['distribuicao']['uma_estrela'], 1)

	def test_should_retornar_ultimas_avaliacoes_em_ordem(self):
		# Arrange
		avaliacoes = [
			self._create_avaliacao(1.0),
			self._create_avaliacao(2.0),
			self._create_avaliacao(3.0),
			self._create_avaliacao(4.0),
		]
		serializer = self._make_serializer()

		# Act
		ultimas = serializer.get_ultimas_avaliacoes(self.servico)

		# Assert
		self.assertEqual(len(ultimas), 3)
		self.assertEqual(ultimas[0]['id'], avaliacoes[-1].id)

	def test_should_retornar_links_relativos_quando_sem_request(self):
		# Arrange
		serializer = self._make_serializer()

		# Act
		links = serializer.get_links(self.servico)

		# Assert
		self.assertEqual(links['avaliacoes'], f'/api/servicos/{self.servico.id}/avaliacoes/')
		self.assertEqual(
			links['categoria'],
			f'/api/servicos/categoria/{self.servico.categoria.id}/'
		)

	def test_should_retornar_links_absolutos_quando_request(self):
		# Arrange
		request = self.factory.get('/')
		serializer = self._make_serializer(request=request)

		# Act
		links = serializer.get_links(self.servico)

		# Assert
		self.assertIn('http://testserver/', links['avaliacoes'])
		self.assertIn('/api/servicos/', links['avaliacoes'])
		self.assertIn('http://testserver/', links['categoria'])
		self.assertIn('/api/servicos/categoria/', links['categoria'])
