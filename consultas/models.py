from django.db import models
from usuarios.models import Usuario

class Status(models.TextChoices):
    AGENDADA = 'agendada', 'Agendada'
    CANCELADA ='cancelada', 'Cancelada'
    REALIZADA = 'realizada', 'Realizada'

class Consulta(models.Model):
    medico = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas_medico')
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas_paciente')
    data = models.DateField()
    anotacao = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.AGENDADA)