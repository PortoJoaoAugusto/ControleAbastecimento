from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class Funcionario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)

    def __str__(self):
        return self.nome

class Abastecimento(models.Model):
    data = models.DateField()
    quantidadelitros = models.PositiveSmallIntegerField()
    km_odometro = models.PositiveSmallIntegerField()

class Veiculo(models.Model):
    placa = models.CharField(max_length=8)
    descricao = models.CharField(max_length=100)
    capacidadetanque = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.placa

class Bomba(models.Model):
    tipocombustivel = models.CharField(max_length=100)
    quantidadedeestoque = models.PositiveSmallIntegerField()
    capacidadebomba = models.PositiveSmallIntegerField()

class CompraCombustivel(models.Model):
    data = models.DateField()
    quantidadelitros = models.PositiveSmallIntegerField()
    precolitro = models.DecimalField(max_digits=5, decimal_places=2)
