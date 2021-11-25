from django import forms
from django.forms import fields, models
from .models import Pessoa, Contato

class PessoaForm(forms.ModelForm):
    data_nascimento = forms.DateField(
        widget=forms.TextInput(
            attrs={"type":"date"}
        )
    )
    class Meta:
        model = Pessoa
        #fields = ('_all_') "TODOS OS CAMPOS" ou 
        fields = ['nome_completo', 'data_nascimento', 'ativo']


class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'telefone']