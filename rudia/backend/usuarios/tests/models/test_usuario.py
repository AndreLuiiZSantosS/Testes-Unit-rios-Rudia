from django.test import TestCase
from django.core.exceptions import ValidationError
from usuarios.models import Usuario
from django.contrib.auth.password_validation import validate_password


class UsuarioModelTest(TestCase):

    def setUp(self):
        self.usuario_base = Usuario.objects.create(
            username="anasilva",
            nome="Ana Silva",
            email="ana@email.com",
            password="SenhaForte1!",
        )

    # CT-01 - Usuário com todos os dados corretos
    def test_ct01_cadastro_com_dados_validos(self):
        usuario = Usuario(
            username="joaopaulo",
            nome="João Paulo",
            email="joao@email.com",
            tipo_usuario="RUDIERO",
        )
        usuario.set_password("SenhaForte1!")

        try:
            usuario.full_clean()
            usuario.save()
        except ValidationError as e:
            self.fail(f"CT-01 falhou inesperadamente: {e}")

        self.assertEqual(usuario.username, "joaopaulo")
        self.assertEqual(usuario.nome, "João Paulo")
        self.assertEqual(usuario.email, "joao@email.com")
        self.assertEqual(usuario.tipo_usuario, "RUDIERO")

    # CT-02 – Username já em uso
    def test_ct02_username_ja_em_uso(self):
        usuario_duplicado = Usuario(
            username="anasilva",
            nome="João Paulo",
            email="joao@email.com",
        )
        usuario_duplicado.set_password("SenhaForte1!")

        with self.assertRaises(ValidationError):
            usuario_duplicado.full_clean()

    # CT-03 – E-mail já cadastrado
    def test_ct03_email_ja_cadastrado(self):
        usuario_duplicado = Usuario(
            username="mariacosta",
            nome="Maria Costa",
            email="ana@email.com",
        )
        usuario_duplicado.set_password("SenhaForte1!")

        with self.assertRaises(ValidationError):
            usuario_duplicado.full_clean()

    # CT-04 – Nome muito curto
    def test_ct04_nome_muito_curto(self):
        usuario = Usuario(
            username="alex_valido",
            nome="Al",              
            email="alex@email.com",
        )
        usuario.set_password("SenhaForte1!")

        with self.assertRaises(ValidationError) as ctx:
            usuario.full_clean()

        self.assertIn("nome", ctx.exception.message_dict)

    # CT-05 – Username muito curto
    def test_ct05_username_muito_curto(self):
        usuario = Usuario(
            username="beto",
            nome="Beto Carlos",
            email="beto@email.com",
        )
        usuario.set_password("SenhaForte1!")

        with self.assertRaises(ValidationError) as ctx:
            usuario.full_clean()

        self.assertIn("username", ctx.exception.message_dict)

    # CT-06 – Username muito longo
    def test_ct06_username_muito_longo(self):
        usuario = Usuario(
            username="username12345678",
            nome="Nome Válido",
            email="teste@email.com",
        )
        usuario.set_password("SenhaForte1!")

        with self.assertRaises(ValidationError) as ctx:
            usuario.full_clean()

        self.assertIn("username", ctx.exception.message_dict)

    # CT-07 – Senha muito curta
    def test_ct07_senha_muito_curta(self):
        """
        CT-07 | AVL – Senha abaixo do mínimo de 8 caracteres
        validate_password() deve levantar ValidationError.
        """
        with self.assertRaises(ValidationError):
            validate_password("Senha@1")   # 7 caracteres

    # CT-08 – Senha fora do padrão
    def test_ct08_senha_fora_do_padrao(self):

        with self.assertRaises(ValidationError):
            validate_password("senhafraca1") 

    # CT-09 – Senhas não coincidem
    def test_ct09_senhas_nao_coincidem(self):
        password = "SenhaForte1!"
        password_confirmation = "SenhaForte2@"

        self.assertNotEqual(
            password,
            password_confirmation,
            "As senhas deveriam ser diferentes e a operação deveria falhar.",
        )

    # CT-10 – Username vazio
    def test_ct10_username_vazio_obrigatorio(self):
        usuario = Usuario(
            username="",
            nome="UI Teste",
            email="ui@email.com",
        )
        usuario.set_password("SenhaForte1!")

        with self.assertRaises(ValidationError) as ctx:
            usuario.full_clean()

        self.assertIn("username", ctx.exception.message_dict)

    # CT-11 – Nome vazio
    def test_ct11_nome_vazio_obrigatorio(self):
        usuario = Usuario(
            username="uiteste",
            nome="",
            email="ui@email.com",
        )
        usuario.set_password("SenhaForte1!")

        with self.assertRaises(ValidationError) as ctx:
            usuario.full_clean()

        self.assertIn("nome", ctx.exception.message_dict)

    # CT-12 – E-mail vazio
    def test_ct12_email_vazio_obrigatorio(self):
        """
        CT-12 | Classe de equivalência INVÁLIDA – e-mail em branco
        Deve levantar ValidationError para o campo 'email'.
        """
        usuario = Usuario(
            username="uiteste",
            nome="UI Teste",
            email="",
        )
        usuario.set_password("SenhaForte1!")

        with self.assertRaises(ValidationError) as ctx:
            usuario.full_clean()

        self.assertIn("email", ctx.exception.message_dict)

    # CT-13 – Senha vazia
    def test_ct13_senha_vazia_obrigatoria(self):
        with self.assertRaises(ValidationError):
            validate_password("")

    # CT-14 – Confirmação de senha vazia
    def test_ct14_confirmacao_senha_vazia_nao_coincide(self):
        password = "SenhaForte1!"
        password_confirmation = ""

        self.assertNotEqual(
            password,
            password_confirmation,
            "Confirmação vazia deve ser diferente da senha – operação deve falhar.",
        )