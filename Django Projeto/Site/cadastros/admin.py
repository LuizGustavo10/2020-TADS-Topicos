from django.contrib import admin
from .models import Pessoa, Funcionario, Ficha

# Register your models here.

admin.site.register(Pessoa)
admin.site.register(Funcionario)
admin.site.register(Ficha)
