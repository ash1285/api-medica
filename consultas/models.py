from django.db import models
from usuarios.models import Usuario

class Consulta(models.Model):
    medico = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas_medico')
    paciente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='consultas_paciente')
    data = models.DateField()
    anotacao = models.TextField()