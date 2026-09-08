from django.db import models
from django.contrib.auth.models import AbstractUser


class Papel(models.TextChoices):
    MEDICO = 'medico', 'Médico'
    PACIENTE = 'paciente', 'Paciente'

class Especialidade(models.TextChoices):
    ORTOPEDISTA = 'ortopedista', 'Ortopedista'
    CARDIOLOGISTA = 'cardiologista', 'Cardiologista'
    NEUROLOGISTA = 'neurologista', 'Neurologista'

class Usuario(AbstractUser):
    nif = models.CharField(max_length=9, unique=True)
    USERNAME_FIELD = "nif"
    papel = models.CharField(max_length=10, choices=Papel.choices)
    especialidade = models.CharField(max_length=30, blank=True, choices=Especialidade.choices) 
    username = None
    REQUIRED_FIELDS =[]