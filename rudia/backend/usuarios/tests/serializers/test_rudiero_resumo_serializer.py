from django.test import TestCase
from datetime import date
from usuarios.models import Rudiero
from usuarios.serializers import RudieroResumoSerializer


class RudieroResumoSerializerTest(TestCase):

    def setUp(self):
        self.rudiero_base = Rudiero.objects.create_user(
            username="anasilva",
            nome="Ana Silva",
            email="ana@email.com",
            password="SenhaForte1!",
            data_nascimento=date(1995, 6, 15),
        )

    # CT-01 – Saída contém exatamente os campos esperados
    def test_ct01_saida_contem_campos_esperados(self):
        serializer = RudieroResumoSerializer(instance=self.rudiero_base)
        data = serializer.data

        campos_esperados = ["id", "username", "nome", "email"]

        for campo in campos_esperados:
            self.assertIn(campo, data)

    # CT-02 – Saída não contém campos além dos permitidos
    def test_ct02_saida_nao_contem_campos_extras(self):
        serializer = RudieroResumoSerializer(instance=self.rudiero_base)
        data = serializer.data

        campos_nao_esperados = [
            "password", "telefone", "foto_perfil",
            "url_instagram", "url_facebook", "url_x", "url_tiktok",
            "data_nascimento", "genero", "tipo_usuario",
            "date_joined", "last_login",
        ]

        for campo in campos_nao_esperados:
            self.assertNotIn(campo, data)

    # CT-03 – Dados do Rudiero são serializados corretamente
    def test_ct03_dados_serializados_corretamente(self):
        serializer = RudieroResumoSerializer(instance=self.rudiero_base)
        data = serializer.data

        self.assertEqual(data["username"], "anasilva")
        self.assertEqual(data["nome"], "Ana Silva")
        self.assertEqual(data["email"], "ana@email.com")
        self.assertIsNotNone(data["id"])

    # CT-04 – id é read_only (ignorado se passado como entrada)
    def test_ct04_id_e_read_only(self):
        dados = {"id": 9999}

        serializer = RudieroResumoSerializer(
            instance=self.rudiero_base,
            data=dados,
            partial=True,
        )
        serializer.is_valid()

        self.assertNotIn("id", serializer.validated_data)

    # CT-05 – Serializer funciona corretamente para múltiplos Rudieros (many=True)
    def test_ct05_serializacao_de_lista(self):
        Rudiero.objects.create_user(
            username="betocosta",
            nome="Beto Costa",
            email="beto@email.com",
            password="SenhaForte1!",
            data_nascimento=date(1990, 1, 1),
        )

        rudieros = Rudiero.objects.all()
        serializer = RudieroResumoSerializer(instance=rudieros, many=True)
        data = serializer.data

        self.assertEqual(len(data), 2)
        usernames = [r["username"] for r in data]
        self.assertIn("anasilva", usernames)
        self.assertIn("betocosta", usernames)