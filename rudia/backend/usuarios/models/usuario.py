from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

class UsuarioManager(UserManager):
    def create_superuser(self, username, email=None, password=None, **extra_fields):
        """Cria um superusuário com tipo ADMINISTRADOR"""
        extra_fields.setdefault('tipo_usuario', Usuario.TipoUsuario.ADMINISTRADOR)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser deve ter is_superuser=True.')
        
        return self.create_user(username, email, password, **extra_fields)

class Usuario(AbstractUser):
    class TipoUsuario(models.TextChoices):
        RUDIERO = 'RUDIERO', 'Rudiero'
        PARCEIRO = 'PARCEIRO', 'Parceiro'
        MODERADOR = 'MODERADOR', 'Moderador'
        ADMINISTRADOR = 'ADMINISTRADOR', 'Administrador'
    
    nome = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True, null=True, unique=True)
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)
    url_instagram = models.URLField(blank=True, null=True, unique=True)
    url_facebook = models.URLField(blank=True, null=True, unique=True)
    url_x = models.URLField(blank=True, null=True, unique=True)
    url_tiktok = models.URLField(blank=True, null=True, unique=True)
    tipo_usuario = models.CharField(
        max_length=20,
        choices=TipoUsuario.choices,
        default=TipoUsuario.RUDIERO
    )

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nome']

    def __str__(self) -> str:
        return f'@{self.username} ({self.get_tipo_usuario_display()})'
    
    class Meta:
        db_table = 'usuario'
        ordering = ['username']
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'