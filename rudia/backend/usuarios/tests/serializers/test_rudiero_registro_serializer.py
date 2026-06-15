from django.test import TestCase
from datetime import date
from dateutil.relativedelta import relativedelta
from usuarios.models import Rudiero
from usuarios.serializers import RudieroRegistroSerializer


class RudieroRegistroSerializerTest(TestCase):

    def setUp(self):
        self.rudiero_base = Rudiero.objects.create_user(
            username="anasilva",
            nome="Ana Silva",
            email="ana@email.com",
            password="SenhaForte1!",
            data_nascimento=date(1995, 6, 15),
            genero="F",
        )

        self.dados_validos = {
            "username": "joaopaulo",
            "nome": "João Paulo",
            "email": "joao@email.com",
            "password": "SenhaForte1!",
            "password_confirm": "SenhaForte1!",
            "data_nascimento": date(1995, 3, 20),
            "genero": "M",
        }

    # CT-01 – Entrada válida cria Rudiero com sucesso
    def test_ct01_entrada_valida_cria_rudiero(self):
        serializer = RudieroRegistroSerializer(data=self.dados_validos)

        self.assertTrue(serializer.is_valid(), serializer.errors)

        rudiero = serializer.save()

        self.assertEqual(rudiero.username, "joaopaulo")
        self.assertEqual(rudiero.nome, "João Paulo")
        self.assertEqual(rudiero.email, "joao@email.com")
        self.assertEqual(rudiero.data_nascimento, date(1995, 3, 20))
        self.assertEqual(rudiero.genero, "M")

    # CT-02 – password_confirm não é salvo no banco
    def test_ct02_password_confirm_nao_salvo(self):
        serializer = RudieroRegistroSerializer(data=self.dados_validos)

        self.assertTrue(serializer.is_valid(), serializer.errors)

        rudiero = serializer.save()

        self.assertFalse(hasattr(rudiero, "password_confirm"))

    # CT-03 – Senha é hasheada (não salva em texto puro)
    def test_ct03_senha_e_hasheada(self):
        serializer = RudieroRegistroSerializer(data=self.dados_validos)

        self.assertTrue(serializer.is_valid(), serializer.errors)

        rudiero = serializer.save()

        self.assertNotEqual(rudiero.password, "SenhaForte1!")
        self.assertTrue(rudiero.check_password("SenhaForte1!"))

    # CT-04 – password e password_confirm são write_only (não aparecem na saída)
    def test_ct04_password_nao_aparece_na_saida(self):
        serializer = RudieroRegistroSerializer(instance=self.rudiero_base)
        data = serializer.data

        self.assertNotIn("password", data)
        self.assertNotIn("password_confirm", data)

    # CT-05 – E-mail duplicado é rejeitado
    def test_ct05_email_duplicado_rejeitado(self):
        dados = {**self.dados_validos, "email": "ana@email.com"}

        serializer = RudieroRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    # CT-06 – Senhas não coincidem
    def test_ct06_senhas_nao_coincidem(self):
        dados = {**self.dados_validos, "password_confirm": "SenhaForte2@"}

        serializer = RudieroRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("password_confirm", serializer.errors)

    # CT-07 – AVL: idade exatamente no limite mínimo (13 anos hoje) é aceita
    def test_ct07_idade_exatamente_13_anos_aceita(self):
        nascimento_limite = date.today() - relativedelta(years=13)
        dados = {**self.dados_validos, "data_nascimento": nascimento_limite}

        serializer = RudieroRegistroSerializer(data=dados)

        self.assertTrue(serializer.is_valid(), serializer.errors)

    # CT-08 – AVL: idade 1 dia abaixo do limite (13 anos - 1 dia) é rejeitada
    def test_ct08_idade_abaixo_do_limite_rejeitada(self):
        nascimento_abaixo = date.today() - relativedelta(years=13) + relativedelta(days=1)
        dados = {**self.dados_validos, "data_nascimento": nascimento_abaixo}

        serializer = RudieroRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("data_nascimento", serializer.errors)

    # CT-09 – AVL: idade acima do limite mínimo (14 anos) é aceita
    def test_ct09_idade_acima_do_limite_aceita(self):
        nascimento_valido = date.today() - relativedelta(years=14)
        dados = {**self.dados_validos, "data_nascimento": nascimento_valido}

        serializer = RudieroRegistroSerializer(data=dados)

        self.assertTrue(serializer.is_valid(), serializer.errors)

    # CT-10 – data_nascimento obrigatória
    def test_ct10_data_nascimento_obrigatoria(self):
        dados = {**self.dados_validos}
        dados.pop("data_nascimento")

        serializer = RudieroRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("data_nascimento", serializer.errors)

    # CT-11 – genero padrão é 'N' quando não informado
    def test_ct11_genero_padrao_prefiro_nao_informar(self):
        dados = {**self.dados_validos}
        dados.pop("genero")

        serializer = RudieroRegistroSerializer(data=dados)

        self.assertTrue(serializer.is_valid(), serializer.errors)

        rudiero = serializer.save()

        self.assertEqual(rudiero.genero, "N")

    # CT-12 – username obrigatório
    def test_ct12_username_obrigatorio(self):
        dados = {**self.dados_validos}
        dados.pop("username")

        serializer = RudieroRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)

    # CT-13 – nome obrigatório
    def test_ct13_nome_obrigatorio(self):
        dados = {**self.dados_validos}
        dados.pop("nome")

        serializer = RudieroRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("nome", serializer.errors)

    # CT-14 – email obrigatório
    def test_ct14_email_obrigatorio(self):
        dados = {**self.dados_validos}
        dados.pop("email")

        serializer = RudieroRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    # CT-15 – password obrigatório
    def test_ct15_password_obrigatorio(self):
        dados = {**self.dados_validos}
        dados.pop("password")

        serializer = RudieroRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)

    # CT-16 – password_confirm obrigatório
    def test_ct16_password_confirm_obrigatorio(self):
        dados = {**self.dados_validos}
        dados.pop("password_confirm")

        serializer = RudieroRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("password_confirm", serializer.errors)