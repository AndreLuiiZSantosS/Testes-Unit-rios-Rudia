from django.contrib import admin
from .models import Cidade, Endereco, Estado, ImagemCidade

admin.site.register(Cidade)
admin.site.register(Endereco)
admin.site.register(Estado)
admin.site.register(ImagemCidade)