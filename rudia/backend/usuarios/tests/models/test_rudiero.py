from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import date, timedelta
from usuarios.models import Rudiero


class RudieroModelTest(TestCase):

    def setUp(self):
        self.rudiero_base = Rudiero.objects.create(
            username="anasilva",
            nome="Ana Silva",
            email="ana@email.com",
            password="SenhaForte1!",
            data_nascimento=date(1995, 6, 15),
            genero="F",
        )

    # CT-01 – Rudiero com todos os dados válidos
    def test_ct01_cadastro_com_dados_validos(self):
        rudiero = Rudiero(
            username="joaopaulo",
            nome="João Paulo",
            email="joao@email.com",
            data_nascimento=date(1990, 3, 20),
            genero="M",
        )
        rudiero.set_password("SenhaForte1!")

        try:
            rudiero.full_clean()
            rudiero.save()
        except ValidationError as e:
            self.fail(f"CT-01 falhou inesperadamente: {e}")

        self.assertEqual(rudiero.username, "joaopaulo")
        self.assertEqual(rudiero.nome, "João Paulo")
        self.assertEqual(rudiero.email, "joao@email.com")
        self.assertEqual(rudiero.data_nascimento, date(1990, 3, 20))
        self.assertEqual(rudiero.genero, "M")

    # CT-02 – data_nascimento vazia (campo obrigatório)
    def test_ct02_data_nascimento_vazia(self):
        rudiero = Rudiero(
            username="betocosta",
            nome="Beto Costa",
            email="beto@email.com",
            data_nascimento=None,
            genero="M",
        )
        rudiero.set_password("SenhaForte1!")

        with self.assertRaises(ValidationError) as ctx:
            rudiero.full_clean()

        self.assertIn("data_nascimento", ctx.exception.message_dict)

    # CT-03 – data_nascimento no futuro
    def test_ct03_data_nascimento_no_futuro(self):
        data_futura = date.today() + timedelta(days=1)

        rudiero = Rudiero(
            username="betocosta",
            nome="Beto Costa",
            email="beto@email.com",
            data_nascimento=data_futura,
            genero="M",
        )
        rudiero.set_password("SenhaForte1!")

        with self.assertRaises(ValidationError) as ctx:
            rudiero.full_clean()

        self.assertIn("data_nascimento", ctx.exception.message_dict)

    # CT-04 – genero com valor fora das choices
    def test_ct04_genero_valor_invalido(self):
        rudiero = Rudiero(
            username="betocosta",
            nome="Beto Costa",
            email="beto@email.com",
            data_nascimento=date(1995, 1, 1),
            genero="X",
        )
        rudiero.set_password("SenhaForte1!")

        with self.assertRaises(ValidationError) as ctx:
            rudiero.full_clean()

        self.assertIn("genero", ctx.exception.message_dict)

    # CT-05 – genero padrão deve ser 'N' (Prefiro Não Informar)
    def test_ct05_genero_padrao_prefiro_nao_informar(self):
        rudiero = Rudiero(
            username="betocosta",
            nome="Beto Costa",
            email="beto@email.com",
            data_nascimento=date(1995, 1, 1),
        )
        rudiero.set_password("SenhaForte1!")

        try:
            rudiero.full_clean()
            rudiero.save()
        except ValidationError as e:
            self.fail(f"CT-05 falhou inesperadamente: {e}")

        self.assertEqual(rudiero.genero, "N")

    # CT-06 – save() deve forçar tipo_usuario como RUDIERO
    def test_ct06_tipo_usuario_sempre_rudiero(self):
        rudiero = Rudiero(
            username="betocosta",
            nome="Beto Costa",
            email="beto@email.com",
            data_nascimento=date(1995, 1, 1),
            genero="M",
            tipo_usuario="ADMINISTRADOR",
        )
        rudiero.set_password("SenhaForte1!")
        rudiero.full_clean()
        rudiero.save()

        self.assertEqual(rudiero.tipo_usuario, "RUDIERO")

    # CT-07 – __str__ deve retornar 'Rudiero: @username'
    def test_ct07_str_retorna_formato_esperado(self):
        resultado = str(self.rudiero_base)
        self.assertEqual(resultado, "Rudiero: @anasilva")