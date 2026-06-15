from django.test import TestCase
from usuarios.models import Usuario
from usuarios.serializers import UsuarioDetalheSerializer


class UsuarioDetalheSerializerTest(TestCase):

    def setUp(self):
        self.usuario_base = Usuario.objects.create_user(
            username="anasilva",
            nome="Ana Silva",
            email="ana@email.com",
            password="SenhaForte1!",
            tipo_usuario="RUDIERO",
        )

    # CT-01 – Saída contém todos os campos esperados
    def test_ct01_saida_contem_campos_esperados(self):
        serializer = UsuarioDetalheSerializer(instance=self.usuario_base)
        data = serializer.data

        campos_esperados = [
            "id", "username", "email", "nome", "telefone",
            "foto_perfil", "url_instagram", "url_facebook",
            "url_x", "url_tiktok", "tipo_usuario",
            "tipo_usuario_display", "date_joined", "last_login",
        ]

        for campo in campos_esperados:
            self.assertIn(campo, data)

    # CT-02 – Dados do usuário são serializados corretamente
    def test_ct02_dados_serializados_corretamente(self):
        serializer = UsuarioDetalheSerializer(instance=self.usuario_base)
        data = serializer.data

        self.assertEqual(data["username"], "anasilva")
        self.assertEqual(data["nome"], "Ana Silva")
        self.assertEqual(data["email"], "ana@email.com")
        self.assertEqual(data["tipo_usuario"], "RUDIERO")

    # CT-03 – tipo_usuario_display retorna o label legível
    def test_ct03_tipo_usuario_display_retorna_label(self):
        serializer = UsuarioDetalheSerializer(instance=self.usuario_base)
        data = serializer.data

        self.assertEqual(data["tipo_usuario_display"], "Rudiero")

    # CT-04 – tipo_usuario_display muda conforme o tipo do usuário
    def test_ct04_tipo_usuario_display_moderador(self):
        moderador = Usuario.objects.create_user(
            username="modsilva",
            nome="Mod Silva",
            email="mod@email.com",
            password="SenhaForte1!",
            tipo_usuario="MODERADOR",
        )

        serializer = UsuarioDetalheSerializer(instance=moderador)
        data = serializer.data

        self.assertEqual(data["tipo_usuario_display"], "Moderador")

    # CT-05 – password não aparece na saída
    def test_ct05_password_nao_aparece_na_saida(self):
        serializer = UsuarioDetalheSerializer(instance=self.usuario_base)
        data = serializer.data

        self.assertNotIn("password", data)

    # CT-06 – Campos opcionais ausentes retornam null sem erro
    def test_ct06_campos_opcionais_nulos_sem_erro(self):
        serializer = UsuarioDetalheSerializer(instance=self.usuario_base)

        try:
            data = serializer.data
        except Exception as e:
            self.fail(f"CT-06 falhou inesperadamente: {e}")

        self.assertIsNone(data["telefone"])
        self.assertIsNone(data["url_instagram"])
        self.assertIsNone(data["url_facebook"])
        self.assertIsNone(data["url_x"])
        self.assertIsNone(data["url_tiktok"])

    # CT-07 – Campos opcionais preenchidos aparecem corretamente na saída
    def test_ct07_campos_opcionais_preenchidos(self):
        usuario = Usuario.objects.create_user(
            username="betocosta",
            nome="Beto Costa",
            email="beto@email.com",
            password="SenhaForte1!",
            tipo_usuario="RUDIERO",
            telefone="84999999999",
            url_instagram="https://instagram.com/beto",
        )

        serializer = UsuarioDetalheSerializer(instance=usuario)
        data = serializer.data

        self.assertEqual(data["telefone"], "84999999999")
        self.assertEqual(data["url_instagram"], "https://instagram.com/beto")

    # CT-08 – tipo_usuario é read_only (ignorado se passado como entrada)
    def test_ct08_tipo_usuario_e_read_only(self):
        dados_entrada = {
            "username": "anasilva",
            "nome": "Ana Silva",
            "email": "ana@email.com",
            "tipo_usuario": "ADMINISTRADOR",
        }

        serializer = UsuarioDetalheSerializer(
            instance=self.usuario_base,
            data=dados_entrada,
            partial=True,
        )
        serializer.is_valid()

        # tipo_usuario não deve estar nos dados validados
        self.assertNotIn("tipo_usuario", serializer.validated_data)

    # CT-09 – id é read_only (ignorado se passado como entrada)
    def test_ct09_id_e_read_only(self):
        dados_entrada = {"id": 9999}

        serializer = UsuarioDetalheSerializer(
            instance=self.usuario_base,
            data=dados_entrada,
            partial=True,
        )
        serializer.is_valid()

        self.assertNotIn("id", serializer.validated_data)

    # CT-10 – date_joined e last_login aparecem na saída
    def test_ct10_date_joined_e_last_login_na_saida(self):
        serializer = UsuarioDetalheSerializer(instance=self.usuario_base)
        data = serializer.data

        self.assertIn("date_joined", data)
        self.assertIsNotNone(data["date_joined"])
        # last_login é None até o primeiro login
        self.assertIn("last_login", data)