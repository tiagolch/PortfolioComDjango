from django.contrib import admin
from .models import *

@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    list_display = ['nome_projeto', 'descricao', 'endereco', 'codigo', 'data_cadastro', 'ativo']
    list_editable = ['ativo']
    list_filter = ['ativo', 'tecnologias']
    search_fields = ['nome_projeto', 'tecnologias']
