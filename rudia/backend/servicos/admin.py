from django.contrib import admin
from .models import Servico, Categoria, Tag, HorarioFuncionamento, ImagemServico

admin.site.register(Servico)
admin.site.register(Categoria)
admin.site.register(Tag)
admin.site.register(HorarioFuncionamento)
admin.site.register(ImagemServico)