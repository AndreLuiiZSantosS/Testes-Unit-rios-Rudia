from django.test import TestCase
from rest_framework.test import APIRequestFactory
from moderacao.models import Proposta
from usuarios.models import Parceiro 
from usuarios.serializers import ParceiroRegistroSerializer

class ParceiroRegistroSerializerTest(TestCase):
    def setUp(self):
        self.dados_validos = {
            'username': 'parceiro_teste',
            'email': 'teste@parceiro.com',
            'password': 'SenhaForte123!',
            'password_confirm': 'SenhaForte123!',
            'nome': 'Empresa Teste',
            'cnpj': '12.345.678/0001-90' # 14 digitos
        }

    def test_registro_valido_cria_parceiro_e_proposta(self):
        serializer = ParceiroRegistroSerializer(data=self.dados_validos)
        self.assertTrue(serializer.is_valid(), serializer.errors)
        parceiro = serializer.save()
        self.assertFalse(parceiro.ativo)
        self.assertEqual(parceiro.email, 'teste@parceiro.com')
        proposta_existe = Proposta.objects.filter(object_id=parceiro.id).exists()
        self.assertTrue(proposta_existe, "A proposta de moderação deveria ter sido criada.")

    def test_validacao_email_duplicado(self):
        Parceiro.objects.create_user(
            username='existente', 
            email='teste@parceiro.com', 
            password='123'
        )        
        serializer = ParceiroRegistroSerializer(data=self.dados_validos)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)

    def test_validacao_senhas_nao_coincidem(self):
        dados = self.dados_validos.copy()
        dados['password_confirm'] = 'SenhaDiferente123!'        
        serializer = ParceiroRegistroSerializer(data=dados)
        self.assertFalse(serializer.is_valid())
        self.assertIn('password_confirm', serializer.errors)

    def test_cnpj_limite_inferior_13_digitos(self):
        dados = self.dados_validos.copy()
        dados['cnpj'] = '1234567890123' # 13 digitos 
        serializer = ParceiroRegistroSerializer(data=dados)
        self.assertFalse(serializer.is_valid())
        self.assertIn('cnpj', serializer.errors)
        self.assertEqual(serializer.errors['cnpj'][0], "CNPJ deve conter 14 dígitos.")

    def test_cnpj_limite_exato_14_digitos(self):
        dados = self.dados_validos.copy()
        dados['cnpj'] = '12345678901234' # 14 digitos so num
        serializer = ParceiroRegistroSerializer(data=dados)
        self.assertTrue(serializer.is_valid(), serializer.errors)

    def test_cnpj_limite_superior_15_digitos(self):
        dados = self.dados_validos.copy()
        dados['cnpj'] = '123456789012345' 
        serializer = ParceiroRegistroSerializer(data=dados)
        self.assertFalse(serializer.is_valid())
        self.assertIn('cnpj', serializer.errors)