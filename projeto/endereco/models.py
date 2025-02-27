from django.db import models


# Create your models here.
class Address(models.Model):
    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length = 50)
    bairro = models.CharField(max_length = 30)
    localiadade = models.CharField(max_length = 30)
    uf = models.CharField(max_length = 2)