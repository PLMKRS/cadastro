from django.db import models


class Pessoa(models.Model):
    nome_completo = models.CharField(max_length=126)
    data_nascimento = models.DateField(null=True)
    ativo = models.BigIntegerField(default=True)