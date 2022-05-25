from django.db import models

# Create your models here.

#[High, Low, Open, Close, Volume, Adj Close]
class Acao(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=10)
    dia = models.DateTimeField()
    high = models.IntegerField()
    low = models.IntegerField()
    open = models.IntegerField()
    close = models.IntegerField()
    volume = models.IntegerField()
    adj_close = models.IntegerField()