from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import Pessoa, Contato


# A rotina abaixo cria os campos na tabela do banco Django-Admin no front-end.

@admin.action(description='Ativar todas as Pessoas')
def ativar_todos(modeladmin, request, queryset):
    queryset.update(ativo=True)


@admin.action(description='Desativar todas as Pessoas')
def desativar_todos(modeladmin, request, queryset):
    queryset.update(ativo=False)

class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome_completo',
        'data_nascimento',
        'ativo'
    ]
    list_filter = [
        'ativo',
        'data_nascimento'
    ]
    search_fields = [
        'nome_completo'
    ]
    actions = [
        ativar_todos,
        desativar_todos
    ]


admin.site.register(Pessoa, PessoaAdmin)
admin.site.register(Contato)