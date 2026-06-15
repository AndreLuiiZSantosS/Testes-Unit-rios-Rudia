from django.test import TestCase
from usuarios.models import Usuario
from usuarios.serializers import UsuarioRegistroSerializer


class UsuarioRegistroSerializerTest(TestCase):

    def setUp(self):
        self.usuario_base = Usuario.objects.create_user(
            username="anasilva",
            nome="Ana Silva",
            email="ana@email.com",
            password="SenhaForte1!",
            tipo_usuario="MODERADOR",
        )

        self.dados_validos = {
            "username": "joaopaulo",
            "nome": "João Paulo",
            "email": "joao@email.com",
            "password": "SenhaForte1!",
            "password_confirm": "SenhaForte1!",
            "tipo_usuario": "MODERADOR",
        }

    # CT-01 – Entrada válida cria usuário com sucesso
    def test_ct01_entrada_valida_cria_usuario(self):
        serializer = UsuarioRegistroSerializer(data=self.dados_validos)

        self.assertTrue(serializer.is_valid(), serializer.errors)

        usuario = serializer.save()

        self.assertEqual(usuario.username, "joaopaulo")
        self.assertEqual(usuario.nome, "João Paulo")
        self.assertEqual(usuario.email, "joao@email.com")
        self.assertEqual(usuario.tipo_usuario, "MODERADOR")

    # CT-02 – password_confirm não é salvo no banco
    def test_ct02_password_confirm_nao_salvo(self):
        serializer = UsuarioRegistroSerializer(data=self.dados_validos)

        self.assertTrue(serializer.is_valid(), serializer.errors)

        usuario = serializer.save()

        self.assertFalse(hasattr(usuario, "password_confirm"))

    # CT-03 – Senha é hasheada (não salva em texto puro)
    def test_ct03_senha_e_hasheada(self):
        serializer = UsuarioRegistroSerializer(data=self.dados_validos)

        self.assertTrue(serializer.is_valid(), serializer.errors)

        usuario = serializer.save()

        self.assertNotEqual(usuario.password, "SenhaForte1!")
        self.assertTrue(usuario.check_password("SenhaForte1!"))

    # CT-04 – password e password_confirm são write_only (não aparecem na saída)
    def test_ct04_password_nao_aparece_na_saida(self):
        serializer = UsuarioRegistroSerializer(instance=self.usuario_base)
        data = serializer.data

        self.assertNotIn("password", data)
        self.assertNotIn("password_confirm", data)

    # CT-05 – E-mail duplicado é rejeitado
    def test_ct05_email_duplicado_rejeitado(self):
        dados = {**self.dados_validos, "email": "ana@email.com"}  # já existe no setUp
        serializer = UsuarioRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    # CT-06 – Senhas não coincidem
    def test_ct06_senhas_nao_coincidem(self):
        dados = {**self.dados_validos, "password_confirm": "SenhaForte2@"}
        serializer = UsuarioRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("password_confirm", serializer.errors)

    # CT-07 – tipo_usuario RUDIERO é rejeitado
    def test_ct07_tipo_usuario_rudiero_rejeitado(self):
        dados = {**self.dados_validos, "tipo_usuario": "RUDIERO"}
        serializer = UsuarioRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("tipo_usuario", serializer.errors)

    # CT-08 – tipo_usuario PARCEIRO é rejeitado
    def test_ct08_tipo_usuario_parceiro_rejeitado(self):
        dados = {**self.dados_validos, "tipo_usuario": "PARCEIRO"}
        serializer = UsuarioRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("tipo_usuario", serializer.errors)

    # CT-09 – tipo_usuario ADMINISTRADOR é aceito
    def test_ct09_tipo_usuario_administrador_aceito(self):
        dados = {**self.dados_validos, "tipo_usuario": "ADMINISTRADOR"}
        serializer = UsuarioRegistroSerializer(data=dados)

        self.assertTrue(serializer.is_valid(), serializer.errors)

        usuario = serializer.save()

        self.assertEqual(usuario.tipo_usuario, "ADMINISTRADOR")

    # CT-10 – username obrigatório
    def test_ct10_username_obrigatorio(self):
        dados = {**self.dados_validos}
        dados.pop("username")
        serializer = UsuarioRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("username", serializer.errors)

    # CT-11 – nome obrigatório
    def test_ct11_nome_obrigatorio(self):
        dados = {**self.dados_validos}
        dados.pop("nome")
        serializer = UsuarioRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("nome", serializer.errors)

    # CT-12 – email obrigatório
    def test_ct12_email_obrigatorio(self):
        dados = {**self.dados_validos}
        dados.pop("email")
        serializer = UsuarioRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("email", serializer.errors)

    # CT-13 – password obrigatório
    def test_ct13_password_obrigatorio(self):
        dados = {**self.dados_validos}
        dados.pop("password")
        serializer = UsuarioRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("password", serializer.errors)

    # CT-14 – password_confirm obrigatório
    def test_ct14_password_confirm_obrigatorio(self):
        dados = {**self.dados_validos}
        dados.pop("password_confirm")
        serializer = UsuarioRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("password_confirm", serializer.errors)

    # CT-15 – tipo_usuario obrigatório
    def test_ct15_tipo_usuario_obrigatorio(self):
        dados = {**self.dados_validos}
        dados.pop("tipo_usuario")
        serializer = UsuarioRegistroSerializer(data=dados)

        self.assertFalse(serializer.is_valid())
        self.assertIn("tipo_usuario", serializer.errors)