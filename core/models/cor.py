from django.db import models


class Cor(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'cor'
        verbose_name_plural = 'cores'
