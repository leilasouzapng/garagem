from django.db import models

from .acessorio import Acessorio
from .cor import Cor
from .modelo import Modelo


class Veiculo(models.Model):
    Ano = models.IntegerField(default=0, null=True, blank=True)
    Preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, blank=True, null=True)
    Modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name='veiculos', null=True, blank=True)
    Cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name='veiculos', null=True, blank=True)
    Acessorio = models.ManyToManyField(Acessorio, related_name='veiculos', null=True, blank=True)

    def __str__(self):
        return f"({self.id}) {self.Modelo} {self.Cor} {self.Ano}"
