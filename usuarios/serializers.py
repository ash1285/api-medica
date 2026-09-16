from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nif', 'papel','password', 'especialidade']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        senha = validated_data.pop('password')
        usuario = Usuario.objects.create(**validated_data)
        usuario.set_password(senha)
        usuario.save()
        return usuario