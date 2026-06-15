from django.test import TestCase
from datetime import date
from usuarios.models import Rudiero
from usuarios.serializers import RudieroDetalheSerializer


class RudieroDetalheSerializerTest(TestCase):

    def setUp(self):
        self.rudiero_base = Rudiero.objects.create_user(
            username="anasilva",
            nome="Ana Silva",
            email="ana@email.com",
            password="SenhaForte1!",
            data_nascimento=date(1995, 6, 15),
            genero="F",
        )

    # CT-01 – Saída contém todos os campos esperados
    def test_ct01_saida_contem_campos_esperados(self):
        serializer = RudieroDetalheSerializer(instance=self.rudiero_base)
        data = serializer.data

        campos_esperados = [
            "id", "username", "email", "nome", "telefone",
            "foto_perfil", "url_instagram", "url_facebook",
            "url_x", "url_tiktok", "data_nascimento",
            "genero", "genero_display", "date_joined", "last_login",
        ]

        for campo in campos_esperados:
            self.assertIn(campo, data)

    # CT-02 – Dados do Rudiero são serializados corretamente
    def test_ct02_dados_serializados_corretamente(self):
        serializer = RudieroDetalheSerializer(instance=self.rudiero_base)
        data = serializer.data

        self.assertEqual(data["username"], "anasilva")
        self.assertEqual(data["nome"], "Ana Silva")
        self.assertEqual(data["email"], "ana@email.com")
        self.assertEqual(data["data_nascimento"], "1995-06-15")
        self.assertEqual(data["genero"], "F")

    # CT-03 – genero_display retorna 'Feminino' para genero 'F'
    def test_ct03_genero_display_feminino(self):
        serializer = RudieroDetalheSerializer(instance=self.rudiero_base)
        data = serializer.data

        self.assertEqual(data["genero_display"], "Feminino")

    # CT-04 – genero_display retorna 'Masculino' para genero 'M'
    def test_ct04_genero_display_masculino(self):
        rudiero = Rudiero.objects.create_user(
            username="betocosta",
            nome="Beto Costa",
            email="beto@email.com",
            password="SenhaForte1!",
            data_nascimento=date(1990, 1, 1),
            genero="M",
        )

        serializer = RudieroDetalheSerializer(instance=rudiero)
        data = serializer.data

        self.assertEqual(data["genero_display"], "Masculino")

    # CT-05 – genero_display retorna 'Outro' para genero 'O'
    def test_ct05_genero_display_outro(self):
        rudiero = Rudiero.objects.create_user(
            username="carlasouza",
            nome="Carla Souza",
            email="carla@email.com",
            password="SenhaForte1!",
            data_nascimento=date(1998, 4, 10),
            genero="O",
        )

        serializer = RudieroDetalheSerializer(instance=rudiero)
        data = serializer.data

        self.assertEqual(data["genero_display"], "Outro")

    # CT-06 – genero_display retorna 'Prefiro Não Informar' para genero 'N'
    def test_ct06_genero_display_prefiro_nao_informar(self):
        rudiero = Rudiero.objects.create_user(
            username="dianatorres",
            nome="Diana Torres",
            email="diana@email.com",
            password="SenhaForte1!",
            data_nascimento=date(2000, 8, 20),
            genero="N",
        )

        serializer = RudieroDetalheSerializer(instance=rudiero)
        data = serializer.data

        self.assertEqual(data["genero_display"], "Prefiro Não Informar")

    # CT-07 – password não aparece na saída
    def test_ct07_password_nao_aparece_na_saida(self):
        serializer = RudieroDetalheSerializer(instance=self.rudiero_base)
        data = serializer.data

        self.assertNotIn("password", data)

    # CT-08 – Campos opcionais ausentes retornam null sem erro
    def test_ct08_campos_opcionais_nulos_sem_erro(self):
        serializer = RudieroDetalheSerializer(instance=self.rudiero_base)

        try:
            data = serializer.data
        except Exception as e:
            self.fail(f"CT-08 falhou inesperadamente: {e}")

        self.assertIsNone(data["telefone"])
        self.assertIsNone(data["url_instagram"])
        self.assertIsNone(data["url_facebook"])
        self.assertIsNone(data["url_x"])
        self.assertIsNone(data["url_tiktok"])

    # CT-09 – Campos opcionais preenchidos aparecem corretamente na saída
    def test_ct09_campos_opcionais_preenchidos(self):
        rudiero = Rudiero.objects.create_user(
            username="betocosta",
            nome="Beto Costa",
            email="beto@email.com",
            password="SenhaForte1!",
            data_nascimento=date(1990, 1, 1),
            genero="M",
            telefone="84999990001",
            url_instagram="https://instagram.com/beto",
        )

        serializer = RudieroDetalheSerializer(instance=rudiero)
        data = serializer.data

        self.assertEqual(data["telefone"], "84999990001")
        self.assertEqual(data["url_instagram"], "https://instagram.com/beto")

    # CT-10 – id é read_only (ignorado se passado como entrada)
    def test_ct10_id_e_read_only(self):
        dados = {"id": 9999}

        serializer = RudieroDetalheSerializer(
            instance=self.rudiero_base,
            data=dados,
            partial=True,
        )
        serializer.is_valid()

        self.assertNotIn("id", serializer.validated_data)

    # CT-11 – date_joined é read_only (ignorado se passado como entrada)
    def test_ct11_date_joined_e_read_only(self):
        dados = {"date_joined": "2000-01-01T00:00:00Z"}

        serializer = RudieroDetalheSerializer(
            instance=self.rudiero_base,
            data=dados,
            partial=True,
        )
        serializer.is_valid()

        self.assertNotIn("date_joined", serializer.validated_data)

    # CT-12 – date_joined e last_login aparecem na saída
    def test_ct12_date_joined_e_last_login_na_saida(self):
        serializer = RudieroDetalheSerializer(instance=self.rudiero_base)
        data = serializer.data

        self.assertIn("date_joined", data)
        self.assertIsNotNone(data["date_joined"])
        self.assertIn("last_login", data)