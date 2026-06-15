from django.contrib import admin
from .models import Roteiro, Viagem, DiaRoteiro

# Register your models here.
admin.site.register(Roteiro)
admin.site.register(Viagem)
admin.site.register(DiaRoteiro)