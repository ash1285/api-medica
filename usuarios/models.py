from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    NIF = models.CharField(max_length=9, unique=True)
    papel = models.CharField(max_length=10)
    especialidade = models.CharField(max_length=30, blank=True)