import shutil
import tempfile
from decimal import Decimal

from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, override_settings
from rest_framework.test import APIRequestFactory

from localizacao.models import Cidade, Endereco, Estado
from servicos.models import Categoria, Servico
from usuarios.models import Rudiero, Usuario, Parceiro
from viagem.serializers import ViagemCreateSerializer


class ViagemCreateSerializerTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.estado = Estado.objects.create(nome='Sao Paulo', sigla='SP')
		cls.cidade = Cidade.objects.create(nome='Campinas', estado=cls.estado)
		cls.cidade_secundaria = Cidade.objects.create(nome='Santos', estado=cls.estado)

		cls.categoria_hospedagem = Categoria.objects.create(nome='Hospedagem')
		cls.categoria_transporte = Categoria.objects.create(nome='Transporte')
		cls.categoria_alimentacao = Categoria.objects.create(nome='Alimentação')
		cls.categoria_lazer = Categoria.objects.create(nome='Lazer')
		cls.categoria_outro = Categoria.objects.create(nome='Outro')

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

	def _create_servico(self, nome, categoria, cidade, ativo=True, capacidade_maxima=None):
		self._endereco_seq += 1
		endereco = Endereco.objects.create(
			cep='12345678',
			logradouro='Rua Teste',
			numero=str(100 + self._endereco_seq)
		)
		return Servico.objects.create(
			nome=nome,
			descricao='Descricao',
			capacidade_maxima=capacidade_maxima,
			preco_minimo=Decimal('100.00'),
			preco_maximo=Decimal('200.00'),
			ativo=ativo,
			imagem_capa=self._make_image_file(f'{nome}.gif'),
			parceiro=self.parceiro,
			categoria=categoria,
			cidade=cidade,
			endereco=endereco,
		)

	def _build_request(self):
		usuario = Usuario.objects.get(pk=self.rudiero.pk)
		request = APIRequestFactory().post('/')
		request.user = usuario
		return request

	def _build_valid_data(self, servicos):
		return {
			'nome': 'Viagem Teste',
			'descricao': 'Descricao valida',
			'dias': 3,
			'viajantes_adultos': 2,
			'viajantes_criancas': 1,
			'visibilidade': 'PRIVADO',
			'cidade_destino': self.cidade.id,
			'hospedagem': servicos['hospedagem'].id,
			'transporte': servicos['transporte'].id,
			'alimentacao': [s.id for s in servicos['alimentacao']],
			'lazer': [s.id for s in servicos['lazer']],
		}

	def _build_valid_servicos(self):
		hospedagem = self._create_servico(
			nome='Hotel',
			categoria=self.categoria_hospedagem,
			cidade=self.cidade,
			capacidade_maxima=10
		)
		transporte = self._create_servico(
			nome='Transporte',
			categoria=self.categoria_transporte,
			cidade=self.cidade,
			capacidade_maxima=10
		)
		alimentacao = [
			self._create_servico(
				nome='Restaurante',
				categoria=self.categoria_alimentacao,
				cidade=self.cidade,
				capacidade_maxima=10
			)
		]
		lazer = [
			self._create_servico(
				nome='Parque',
				categoria=self.categoria_lazer,
				cidade=self.cidade,
				capacidade_maxima=10
			)
		]
		return {
			'hospedagem': hospedagem,
			'transporte': transporte,
			'alimentacao': alimentacao,
			'lazer': lazer,
		}

	def test_should_validar_dados_quando_servicos_validos(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()
		orcamento = serializer.validated_data.get('orcamento_total')

		# Assert
		self.assertTrue(is_valid)
		self.assertEqual(orcamento, Decimal('1800.00'))

	def test_should_criar_viagem_quando_salvar(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)
		serializer.is_valid(raise_exception=True)

		# Act
		viagem = serializer.save()
		servicos_ids = set(viagem.servicos.values_list('id', flat=True))

		# Assert
		self.assertEqual(viagem.rudiero, self.rudiero)
		self.assertEqual(viagem.cidade_destino, self.cidade)
		self.assertEqual(len(servicos_ids), 4)
		self.assertIn(servicos['hospedagem'].id, servicos_ids)
		self.assertIn(servicos['transporte'].id, servicos_ids)
		self.assertIn(servicos['alimentacao'][0].id, servicos_ids)
		self.assertIn(servicos['lazer'][0].id, servicos_ids)

    # Dados da Viagem

	def test_should_rejeitar_nome_longo_quando_maior_150(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data['nome'] = 'A' * 151
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('nome', serializer.errors)

	def test_should_rejeitar_nome_curto_quando_menor_5(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data['nome'] = 'ABCD'
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('nome', serializer.errors)

	def test_should_rejeitar_descricao_curta_quando_menor_10(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data['descricao'] = 'Curta'
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('descricao', serializer.errors)

	def test_should_rejeitar_descricao_longa_quando_maior_500(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data['descricao'] = 'D' * 501
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('descricao', serializer.errors)

	def test_should_rejeitar_dias_quando_menor_igual_zero(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data['dias'] = 0
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('dias', serializer.errors)

	def test_should_validar_extremos_quando_dias_listas_nome_descricao_validos(self):
		# Arrange
		servicos = self._build_valid_servicos()
		servicos['alimentacao'].extend([
			self._create_servico(
				nome='Restaurante B',
				categoria=self.categoria_alimentacao,
				cidade=self.cidade,
				capacidade_maxima=10
			),
			self._create_servico(
				nome='Restaurante C',
				categoria=self.categoria_alimentacao,
				cidade=self.cidade,
				capacidade_maxima=10
			),
		])
		servicos['lazer'].extend([
			self._create_servico(
				nome='Museu',
				categoria=self.categoria_lazer,
				cidade=self.cidade,
				capacidade_maxima=10
			),
			self._create_servico(
				nome='Trilha',
				categoria=self.categoria_lazer,
				cidade=self.cidade,
				capacidade_maxima=10
			),
		])
		data = self._build_valid_data(servicos)
		data['dias'] = 365
		data['nome'] = 'A' * 150
		data['descricao'] = 'D' * 500
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)

	def test_should_rejeitar_viajantes_quando_adultos_ou_criancas_menor_igual_zero(self):
		# Arrange
		servicos = self._build_valid_servicos()
		cases = [
			{
				'viajantes_adultos': 0,
				'viajantes_criancas': 1,
				'field': 'viajantes_adultos',
				'valid': False,
			},
			{
				'viajantes_adultos': 0,
				'viajantes_criancas': 0,
				'field': 'viajantes_adultos',
				'valid': False,
			},
			{
				'viajantes_adultos': -1,
				'viajantes_criancas': 1,
				'field': 'viajantes_adultos',
				'valid': False,
			},
			{
				'viajantes_adultos': 1,
				'viajantes_criancas': -1,
				'field': 'viajantes_criancas',
				'valid': False,
			},
			{
				'viajantes_adultos': 1,
				'viajantes_criancas': 0,
				'field': None,
				'valid': True,
			},
		]

		# Act + Assert
		for case in cases:
			with self.subTest(field=case['field']):
				data = self._build_valid_data(servicos)
				data['viajantes_adultos'] = case['viajantes_adultos']
				data['viajantes_criancas'] = case['viajantes_criancas']
				serializer = ViagemCreateSerializer(
					data=data,
					context={'request': self._build_request()}
				)
				is_valid = serializer.is_valid()
				if case['valid']:
					self.assertTrue(is_valid)
				else:
					self.assertFalse(is_valid)
					self.assertIn(case['field'], serializer.errors)

	def test_should_rejeitar_cidade_destino_quando_ausente_ou_inexistente(self):
		# Arrange
		servicos = self._build_valid_servicos()
		cases = [
			{'cidade_destino': None, 'remove': True},
			{'cidade_destino': 99999, 'remove': False},
		]

		# Act + Assert
		for case in cases:
			with self.subTest(cidade_destino=case['cidade_destino']):
				data = self._build_valid_data(servicos)
				if case['remove']:
					data.pop('cidade_destino')
				else:
					data['cidade_destino'] = case['cidade_destino']
				serializer = ViagemCreateSerializer(
					data=data,
					context={'request': self._build_request()}
				)
				is_valid = serializer.is_valid()
				self.assertFalse(is_valid)
				self.assertIn('cidade_destino', serializer.errors)

	def test_should_rejeitar_cidade_destino_invalida_quando_texto(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data['cidade_destino'] = '###'
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('cidade_destino', serializer.errors)

	def test_should_rejeitar_visibilidade_quando_ausente(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data.pop('visibilidade')
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('visibilidade', serializer.errors)

	def test_should_rejeitar_visibilidade_invalida_quando_fora_dominio(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data['visibilidade'] = 'AMIGOS'
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('visibilidade', serializer.errors)

    # Serviços da Viagem

	def test_should_rejeitar_hospedagem_quando_ausente(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data.pop('hospedagem')
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('hospedagem', serializer.errors)

	def test_should_rejeitar_hospedagem_quando_inexistente(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data['hospedagem'] = 99999
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('hospedagem', serializer.errors)

	def test_should_rejeitar_transporte_quando_ausente(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data.pop('transporte')
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('transporte', serializer.errors)

	def test_should_rejeitar_transporte_quando_inexistente(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data['transporte'] = 99999
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('transporte', serializer.errors)


	def test_should_rejeitar_alimentacao_quando_vazio(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data['alimentacao'] = []
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('alimentacao', serializer.errors)

	def test_should_rejeitar_alimentacao_quando_inexistente(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data['alimentacao'] = [99999]
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('alimentacao', serializer.errors)

	def test_should_rejeitar_lazer_quando_vazio(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data['lazer'] = []
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('lazer', serializer.errors)

	def test_should_rejeitar_lazer_quando_inexistente(self):
		# Arrange
		servicos = self._build_valid_servicos()
		data = self._build_valid_data(servicos)
		data['lazer'] = [99999]
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('lazer', serializer.errors)

	def test_should_rejeitar_categoria_incorreta_quando_hospedagem_invalida(self):
		# Arrange
		servicos = self._build_valid_servicos()
		servicos['hospedagem'] = self._create_servico(
			nome='Onibus',
			categoria=self.categoria_transporte,
			cidade=self.cidade,
			capacidade_maxima=10
		)
		data = self._build_valid_data(servicos)
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('hospedagem', serializer.errors)

	def test_should_rejeitar_servicos_de_cidade_diferente_quando_nao_correspondem(self):
		# Arrange
		servicos = self._build_valid_servicos()
		servicos['transporte'] = self._create_servico(
			nome='Transporte B',
			categoria=self.categoria_transporte,
			cidade=self.cidade_secundaria,
			capacidade_maxima=10
		)
		data = self._build_valid_data(servicos)
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('servicos', serializer.errors)

	def test_should_rejeitar_servicos_sem_capacidade_quando_insuficiente(self):
		# Arrange
		servicos = self._build_valid_servicos()
		servicos['hospedagem'] = self._create_servico(
			nome='Hotel Pequeno',
			categoria=self.categoria_hospedagem,
			cidade=self.cidade,
			capacidade_maxima=1
		)
		data = self._build_valid_data(servicos)
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('servicos', serializer.errors)

	def test_should_rejeitar_servico_inativo_quando_hospedagem_inativa(self):
		# Arrange
		servico_inativo = self._create_servico(
			nome='Hotel Inativo',
			categoria=self.categoria_hospedagem,
			cidade=self.cidade,
			ativo=False,
			capacidade_maxima=10
		)
		servicos = self._build_valid_servicos()
		servicos['hospedagem'] = servico_inativo
		data = self._build_valid_data(servicos)
		serializer = ViagemCreateSerializer(
			data=data,
			context={'request': self._build_request()}
		)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertEqual(
			serializer.errors['hospedagem'][0],
			'Serviço de hospedagem não encontrado ou inativo.'
		)
