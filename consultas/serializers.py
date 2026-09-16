from rest_framework import serializers
from .models import Consulta


class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id', 'medico', 'paciente', 'data', 'anotacao','status']
        
class ConsultaPacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id', 'status']