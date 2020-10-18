from django.db import models

# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50, verbose_name="Endereço")
    telefone = models.IntegerField()
    email = models.CharField(max_length=50)
    cpf = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.nome, self.endereco)

class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    endereco = models.CharField(max_length=50, verbose_name="Endereço")
    telefone = models .IntegerField()
    email = models.CharField(max_length=50)
    cpf = models.IntegerField()

    def __str__(self):
        return "{} ({})".format(self.nome, self.endereco)

class Ficha(models.Model):
    data = models.CharField(max_length=50)
    qtd = models .IntegerField()

    funcionario = models.ForeignKey(Funcionario, on_delete = models.PROTECT)
    pessoa = models.ForeignKey(Pessoa, on_delete = models.PROTECT)
    
    def __str__(self):
        return "{} ({})".format(self.data, self.qtd)