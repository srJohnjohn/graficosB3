from django.db import models

# Create your models here.

#[High, Low, Open, Close, Volume, Adj Close]
class Acao(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=10)
    dia = models.DateTimeField()
    high = models.FloatField()
    low = models.FloatField()
    open = models.FloatField()
    close = models.FloatField()
    volume = models.FloatField()
    adj_close = models.FloatField()

    def __str__(self):
        return f'{self.nome} - {self.codigo}'