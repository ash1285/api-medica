from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager


class Papel(models.TextChoices):
    MEDICO = 'medico', 'Médico'
    PACIENTE = 'paciente', 'Paciente'

class Especialidade(models.TextChoices):
    ORTOPEDISTA = 'ortopedista', 'Ortopedista'
    CARDIOLOGISTA = 'cardiologista', 'Cardiologista'
    NEUROLOGISTA = 'neurologista', 'Neurologista'

class UsuarioManager(BaseUserManager):
    def create_user(self, nif, password=None, **extra_fields):
        usuario = self.model(nif=nif, **extra_fields)
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, nif, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(nif, password, **extra_fields)

class Usuario(AbstractUser):
    nif = models.CharField(max_length=9, unique=True)
    USERNAME_FIELD = "nif"
    papel = models.CharField(max_length=10, choices=Papel.choices)
    especialidade = models.CharField(max_length=30, blank=True, choices=Especialidade.choices) 
    username = None
    REQUIRED_FIELDS =[]
    objects = UsuarioManager()