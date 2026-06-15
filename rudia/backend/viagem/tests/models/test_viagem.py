from decimal import Decimal

from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from localizacao.models import Cidade, Estado
from usuarios.models import Rudiero
from viagem.models import Viagem

class ViagemModelTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.estado = Estado.objects.create(nome='Sao Paulo', sigla='SP')
		cls.cidade = Cidade.objects.create(nome='Campinas', estado=cls.estado)
		cls.rudiero = Rudiero.objects.create_user(
			username='rudiero1',
			email='rudiero1@example.com',
			nome='Rudiero 1',
			password='senha123',
			data_nascimento='1990-01-01',
		)
		cls.viagem = Viagem.objects.create(
			nome='Viagem Base',
			descricao='Descricao base',
			dias=3,
			orcamento_total=Decimal('1500.00'),
			rudiero=cls.rudiero,
			cidade_destino=cls.cidade,
		)

	def _build_viagem_data(self):
		return {
			'nome': 'Viagem Nova',
			'descricao': 'Descricao nova',
			'dias': 5,
			'orcamento_total': Decimal('2500.00'),
			'rudiero': self.rudiero,
			'cidade_destino': self.cidade,
		}

	def test_should_retornar_string_quando_convertido(self):
		# Arrange
		viagem = self.viagem

		# Act
		result = str(viagem)

		# Assert
		self.assertEqual(result, f'Viagem Base - @{self.rudiero.username}')

	def test_should_definir_valores_padrao_quando_criado(self):
		# Arrange
		viagem = self.viagem

		# Act
		viajantes_adultos = viagem.viajantes_adultos
		viajantes_criancas = viagem.viajantes_criancas
		visibilidade = viagem.visibilidade
		data_criacao = viagem.data_criacao

		# Assert
		self.assertEqual(viajantes_adultos, 1)
		self.assertEqual(viajantes_criancas, 0)
		self.assertEqual(visibilidade, Viagem.Visibilidade.PRIVADO)
		self.assertIsNotNone(data_criacao)

	def test_should_validar_campos_obrigatorios_quando_ausentes(self):
		# Arrange
		required_fields = [
			'nome',
			'descricao',
			'dias',
			'orcamento_total',
			'rudiero',
			'cidade_destino',
		]

		# Act + Assert
		for field in required_fields:
			with self.subTest(field=field):
				data = self._build_viagem_data()
				data[field] = None
				viagem = Viagem(**data)
				with self.assertRaises(ValidationError):
					viagem.full_clean()

	def test_should_ordenar_por_nome_e_data_criacao_desc_quando_listado(self):
		# Arrange
		viagem_alpha_1 = Viagem.objects.create(
			nome='Alpha',
			descricao='Primeira',
			dias=2,
			orcamento_total=Decimal('100.00'),
			rudiero=self.rudiero,
			cidade_destino=self.cidade,
		)
		viagem_alpha_2 = Viagem.objects.create(
			nome='Alpha',
			descricao='Segunda',
			dias=4,
			orcamento_total=Decimal('200.00'),
			rudiero=self.rudiero,
			cidade_destino=self.cidade,
		)
		viagem_beta = Viagem.objects.create(
			nome='Beta',
			descricao='Terceira',
			dias=1,
			orcamento_total=Decimal('50.00'),
			rudiero=self.rudiero,
			cidade_destino=self.cidade,
		)

		Viagem.objects.filter(id=viagem_alpha_1.id).update(
			data_criacao=timezone.now() - timezone.timedelta(days=2)
		)
		Viagem.objects.filter(id=viagem_alpha_2.id).update(
			data_criacao=timezone.now() - timezone.timedelta(days=1)
		)

		# Act
		ordered = list(Viagem.objects.all())

		# Assert
		self.assertEqual(ordered[0], viagem_alpha_2)
		self.assertEqual(ordered[1], viagem_alpha_1)
		self.assertEqual(ordered[2], viagem_beta)

	def test_should_manter_relacionamentos_com_rudiero_e_cidade(self):
		# Arrange
		viagem = self.viagem

		# Act
		rudiero_viagens = list(self.rudiero.viagens.all())
		cidade_viagens = list(self.cidade.viagens_destino.all())

		# Assert
		self.assertIn(viagem, rudiero_viagens)
		self.assertIn(viagem, cidade_viagens)

	def test_should_rejeitar_nome_maior_150_quando_validado(self):
		# Arrange
		data = self._build_viagem_data()
		data['nome'] = 'A' * 151
		viagem = Viagem(**data)

		# Act + Assert
		with self.assertRaises(ValidationError):
			viagem.full_clean()
