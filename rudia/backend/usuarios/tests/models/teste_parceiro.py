from django.test import TestCase
from django.db.utils import IntegrityError
from usuarios.models import Parceiro, Usuario

class ParceiroModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.parceiro = Parceiro.objects.create(
            username='joao_silva',
            cnpj='12345678901234'
        )

    def test_cnpj_max_length(self):
        parceiro = Parceiro.objects.get(id=self.parceiro.id)
        max_length = parceiro._meta.get_field('cnpj').max_length
        self.assertEqual(max_length, 14)

    def test_cnpj_is_unique(self):
        with self.assertRaises(IntegrityError):
            Parceiro.objects.create(
                username='maria_santos',
                cnpj='12345678901234' # cnpj repetido
            )

    def test_ativo_default_value(self):
        parceiro = Parceiro.objects.get(id=self.parceiro.id)
        self.assertFalse(parceiro.ativo)

    def test_str_representation_when_ativo_false(self):
        parceiro = Parceiro.objects.get(id=self.parceiro.id)
        expected_object_name = f"Parceiro: @{parceiro.username} - Ativo: NÃO"
        self.assertEqual(str(parceiro), expected_object_name)

    def test_str_representation_when_ativo_true(self):
        parceiro = Parceiro.objects.get(id=self.parceiro.id)
        parceiro.ativo = True
        parceiro.save() # Guarda a alteração
        expected_object_name = f"Parceiro: @{parceiro.username} - Ativo: SIM"
        self.assertEqual(str(parceiro), expected_object_name)

    def test_save_sets_tipo_usuario_correctly(self):
        parceiro = Parceiro.objects.get(id=self.parceiro.id)
        # corrigir acesso
        self.assertEqual(Usuario.tipo_usuario, Usuario.TipoUsuario.PARCEIRO)

    def test_meta_ordering(self):
        ordering = Parceiro._meta.ordering
        self.assertEqual(ordering, ['username'])

    def test_meta_verbose_names(self):
        self.assertEqual(Parceiro._meta.verbose_name, 'Parceiro')
        self.assertEqual(Parceiro._meta.verbose_name_plural, 'Parceiros')