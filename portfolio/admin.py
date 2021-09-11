from django.contrib import admin
from .models import Projetos, Tecnologias

@admin.register(Projetos)
class ProjetosAdmin(admin.ModelAdmin):
    list_display = ['nome_projeto', 'descricao', 'endereco', 'codigo', 'data_cadastro', 'ativo']
    list_editable = ['ativo']
    list_filter = ['ativo', 'tecnologias']
    search_fields = ['nome_projeto', 'tecnologias']
    list_per_page = 10

@admin.register(Tecnologias)
class TecnologiasAdmin(admin.ModelAdmin):
    list_display = ['tecnologia']
    search_fields = ['tecnologia']
    list_per_page = 10
