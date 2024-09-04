from django.db import models

#
from django.db import models

##class Sala(models.Model):
    #nome = models.CharField(max_length=255)
    #capacidade = models.IntegerField()

    #def __str__(self):
        #return self.nome

# modelo de banco de dados de reserva de salas
class Reserva(models.Model):
    sala = models.IntegerField( null=False, blank=False)
    categoria = models.CharField(max_length=100, null=False, blank=False)
    filme = models.CharField(max_length=100, null=False, blank=False)
    data = models.DateField(null=False)
    horario = models.TimeField()
    nome_responsavel = models.CharField(max_length=100)
    email = models.CharField(max_length=100)

    #def __str__(self):
        #return f"Reserva de {self.sala.nome} em {self.data} às {self.hora_inicio} até {self.hora_fim}"
