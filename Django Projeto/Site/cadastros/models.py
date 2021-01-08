from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50, verbose_name="Endereço", unique=True)
    telefone = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    cpf = models.CharField(max_length=50)
    arquivo = models.FileField(upload_to='pdf/')

    def __str__(self):
        return "{} ({})".format(self.nome, self.endereco)

class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50, verbose_name="Endereço", unique=True)
    telefone = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    cpf = models.CharField(max_length=50)

    def __str__(self):
        return "{} ({})".format(self.nome, self.endereco)

class Ficha(models.Model):
    
    data = models.CharField(max_length=50)
    qtd = models .IntegerField()
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)

    funcionario = models.ForeignKey(Funcionario, on_delete = models.PROTECT)
    pessoa = models.ForeignKey(Pessoa, on_delete = models.PROTECT)
    
    def __str__(self):
        return "{} ({})".format(self.data, self.qtd)