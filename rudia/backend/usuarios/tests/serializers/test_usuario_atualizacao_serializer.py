from django.test import TestCase
from usuarios.models import Usuario
from usuarios.serializers import UsuarioAtualizacaoSerializer


class UsuarioAtualizacaoSerializerTest(TestCase):

    def setUp(self):
        self.usuario_base = Usuario.objects.create_user(
            username="anasilva",
            nome="Ana Silva",
            email="ana@email.com",
            password="SenhaForte1!",
            tipo_usuario="RUDIERO",
            telefone="84999990001",
            url_instagram="https://instagram.com/ana",
        )

        self.usuario_secundario = Usuario.objects.create_user(
            username="betocosta",
            nome="Beto Costa",
            email="beto@email.com",
            password="SenhaForte1!",
            tipo_usuario="RUDIERO",
        )

    # CT-01 – Atualização válida salva os campos corretamente
    def test_ct01_atualizacao_valida(self):
        dados = {
            "telefone": "84999990002",
            "url_instagram": "https://instagram.com/novo",
            "url_facebook": "https://facebook.com/novo",
            "url_x": "https://x.com/novo",
            "url_tiktok": "https://tiktok.com/@novo",
        }

        serializer = UsuarioAtualizacaoSerializer(
            instance=self.usuario_secundario,
            data=dados,
            partial=True,
        )

        self.assertTrue(serializer.is_valid(), serializer.errors)

        usuario = serializer.save()

        self.assertEqual(usuario.telefone, "84999990002")
        self.assertEqual(usuario.url_instagram, "https://instagram.com/novo")
        self.assertEqual(usuario.url_facebook, "https://facebook.com/novo")
        self.assertEqual(usuario.url_x, "https://x.com/novo")
        self.assertEqual(usuario.url_tiktok, "https://tiktok.com/@novo")

    # CT-02 – Atualização parcial (somente um campo) funciona
    def test_ct02_atualizacao_parcial_um_campo(self):
        dados = {"telefone": "84999990003"}

        serializer = UsuarioAtualizacaoSerializer(
            instance=self.usuario_secundario,
            data=dados,
            partial=True,
        )

        self.assertTrue(serializer.is_valid(), serializer.errors)

        usuario = serializer.save()

        self.assertEqual(usuario.telefone, "84999990003")

    # CT-03 – Todos os campos podem ser nulos (opcionais)
    def test_ct03_todos_os_campos_nulos_sem_erro(self):
        dados = {
            "telefone": None,
            "foto_perfil": None,
            "url_instagram": None,
            "url_facebook": None,
            "url_x": None,
            "url_tiktok": None,
        }

        serializer = UsuarioAtualizacaoSerializer(
            instance=self.usuario_base,
            data=dados,
        )

        self.assertTrue(serializer.is_valid(), serializer.errors)

        usuario = serializer.save()

        self.assertIsNone(usuario.telefone)
        self.assertIsNone(usuario.url_instagram)
        self.assertIsNone(usuario.url_facebook)
        self.assertIsNone(usuario.url_x)
        self.assertIsNone(usuario.url_tiktok)

    # CT-04 – Telefone duplicado é rejeitado
    def test_ct04_telefone_duplicado_rejeitado(self):
        # usuario_base já usa "84999990001"
        dados = {"telefone": "84999990001"}

        serializer = UsuarioAtualizacaoSerializer(
            instance=self.usuario_secundario,
            data=dados,
            partial=True,
        )

        self.assertFalse(serializer.is_valid())
        self.assertIn("telefone", serializer.errors)

    # CT-05 – url_instagram duplicada é rejeitada
    def test_ct05_url_instagram_duplicada_rejeitada(self):
        # usuario_base já usa essa URL
        dados = {"url_instagram": "https://instagram.com/ana"}

        serializer = UsuarioAtualizacaoSerializer(
            instance=self.usuario_secundario,
            data=dados,
            partial=True,
        )

        self.assertFalse(serializer.is_valid())
        self.assertIn("url_instagram", serializer.errors)

    # CT-06 – username não pode ser alterado por este serializer
    def test_ct06_username_ignorado_na_atualizacao(self):
        dados = {"username": "hacker"}

        serializer = UsuarioAtualizacaoSerializer(
            instance=self.usuario_base,
            data=dados,
            partial=True,
        )
        serializer.is_valid()

        self.assertNotIn("username", serializer.validated_data)

    # CT-07 – email não pode ser alterado por este serializer
    def test_ct07_email_ignorado_na_atualizacao(self):
        dados = {"email": "novo@email.com"}

        serializer = UsuarioAtualizacaoSerializer(
            instance=self.usuario_base,
            data=dados,
            partial=True,
        )
        serializer.is_valid()

        self.assertNotIn("email", serializer.validated_data)

    # CT-08 – tipo_usuario não pode ser alterado por este serializer
    def test_ct08_tipo_usuario_ignorado_na_atualizacao(self):
        dados = {"tipo_usuario": "ADMINISTRADOR"}

        serializer = UsuarioAtualizacaoSerializer(
            instance=self.usuario_base,
            data=dados,
            partial=True,
        )
        serializer.is_valid()

        self.assertNotIn("tipo_usuario", serializer.validated_data)

    # CT-09 – Saída contém apenas os campos permitidos
    def test_ct09_saida_contem_apenas_campos_permitidos(self):
        serializer = UsuarioAtualizacaoSerializer(instance=self.usuario_base)
        data = serializer.data

        campos_esperados = [
            "telefone", "foto_perfil",
            "url_instagram", "url_facebook", "url_x", "url_tiktok",
        ]
        campos_nao_esperados = [
            "id", "username", "email", "nome",
            "tipo_usuario", "password", "date_joined",
        ]

        for campo in campos_esperados:
            self.assertIn(campo, data)

        for campo in campos_nao_esperados:
            self.assertNotIn(campo, data)