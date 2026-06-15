from django.test import TestCase

from localizacao.models import Cidade, Estado
from localizacao.serializers import EstadoDetalheSerializer, EstadoResumoSerializer, EstadoSerializer


class EstadoSerializerTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.estado_sp = Estado.objects.create(nome='Sao Paulo', sigla='SP')
		cls.estado_rj = Estado.objects.create(nome='Rio', sigla='RJ')
		Cidade.objects.create(nome='Campinas', estado=cls.estado_sp)
		Cidade.objects.create(nome='Santos', estado=cls.estado_sp)
		Cidade.objects.create(nome='Niteroi', estado=cls.estado_rj)

	def test_should_normalizar_sigla_quando_valida(self):
		# Arrange
		serializer = EstadoSerializer(data={'nome': 'Minas Gerais', 'sigla': ' mg '})

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)
		self.assertEqual(serializer.validated_data['sigla'], 'MG')

	def test_should_rejeitar_sigla_com_tamanho_invalido(self):
		# Arrange
		serializer = EstadoSerializer(data={'nome': 'Rio', 'sigla': 'R'})

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('sigla', serializer.errors)

	def test_should_rejeitar_sigla_com_caractere_nao_alfabetico(self):
		# Arrange
		serializer = EstadoSerializer(data={'nome': 'Bahia', 'sigla': '1B'})

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertFalse(is_valid)
		self.assertIn('sigla', serializer.errors)

	def test_should_normalizar_nome_quando_valido(self):
		# Arrange
		serializer = EstadoSerializer(data={'nome': '  paraiba  ', 'sigla': 'PB'})

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)
		self.assertEqual(serializer.validated_data['nome'], 'Paraiba')

	def test_should_ignorar_id_somente_leitura_quando_atualizacao_parcial(self):
		# Arrange
		serializer = EstadoSerializer(self.estado_sp, data={'id': 999}, partial=True)

		# Act
		is_valid = serializer.is_valid()

		# Assert
		self.assertTrue(is_valid)
		self.assertNotIn('id', serializer.validated_data)

	def test_should_retornar_total_cidades_quando_serializado(self):
		# Arrange
		serializer = EstadoSerializer(self.estado_sp)

		# Act
		data = serializer.data

		# Assert
		self.assertEqual(data['total_cidades'], 2)

	def test_should_retornar_lista_cidades_quando_serializado(self):
		# Arrange
		serializer = EstadoDetalheSerializer(self.estado_sp)

		# Act
		data = serializer.data

		# Assert
		self.assertEqual(data['total_cidades'], 2)
		self.assertEqual([cidade['nome'] for cidade in data['cidades']], ['Campinas', 'Santos'])

	def test_should_retornar_estado_resumo_quando_serializado(self):
		# Arrange
		serializer = EstadoResumoSerializer(self.estado_sp)

		# Act
		data = serializer.data

		# Assert
		self.assertEqual(data['sigla'], 'SP')
