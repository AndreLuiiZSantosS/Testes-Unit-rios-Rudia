from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from servicos.models import Categoria, Tag, Servico, HorarioFuncionamento
from localizacao.models import Estado, Cidade, Endereco
from usuarios.models import Parceiro


class HorarioFuncionamentoModelTest(TestCase):
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
		estado = Estado.objects.create(nome='Sao Paulo', sigla='SP')
		cidade = Cidade.objects.create(nome='Campinas', estado=estado)
		categoria = Categoria.objects.create(nome='Passeios')
		Tag.objects.create(nome='Aventura', descricao='Ao ar livre', categoria=categoria)
		parceiro = Parceiro.objects.create_user(
			username='parceiro1',
			email='parceiro1@test.com',
			password='12345678',
			nome='Parceiro Um',
			cnpj='12345678901234'
		)
		endereco = Endereco.objects.create(
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
			parceiro=parceiro,
			categoria=categoria,
			cidade=cidade,
			endereco=endereco
		)
		cls.horario_base = HorarioFuncionamento.objects.create(
			hora_abertura='08:00',
			hora_fechamento='17:00',
			dia_semana=HorarioFuncionamento.DiaSemana.SEGUNDA,
			servico=cls.servico
		)

	def test_should_retornar_string_quando_convertido(self):
		# Arrange
		horario = self.horario_base

		# Act
		result = str(horario)

		# Assert
		self.assertEqual(
			result,
			'Horário de Passeio de Barco - Segunda-feira: 08:00 às 17:00'
		)

	def test_should_ordenar_por_servico_e_dia_semana_quando_listado(self):
		# Arrange
		endereco = Endereco.objects.create(
			cep='87654321',
			logradouro='Rua B',
			numero='200'
		)
		servico_b = Servico.objects.create(
			nome='Aventura na Serra',
			descricao='Trilha guiada',
			capacidade_maxima=6,
			preco_minimo='90.00',
			preco_maximo='140.00',
			imagem_capa=self._make_image_file('servico2.gif'),
			parceiro=self.servico.parceiro,
			categoria=self.servico.categoria,
			cidade=self.servico.cidade,
			endereco=endereco
		)
		HorarioFuncionamento.objects.create(
			hora_abertura='09:00',
			hora_fechamento='18:00',
			dia_semana=HorarioFuncionamento.DiaSemana.QUARTA,
			servico=servico_b
		)
		HorarioFuncionamento.objects.create(
			hora_abertura='10:00',
			hora_fechamento='19:00',
			dia_semana=HorarioFuncionamento.DiaSemana.DOMINGO,
			servico=self.servico
		)

		# Act
		ordered = list(HorarioFuncionamento.objects.all())

		# Assert
		self.assertEqual(
			[(item.servico.nome, item.dia_semana) for item in ordered],
			sorted((item.servico.nome, item.dia_semana) for item in ordered)
		)
