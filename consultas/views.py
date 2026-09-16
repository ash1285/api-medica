from rest_framework import viewsets
from .models import Consulta
from .serializers import ConsultaSerializer, ConsultaPacienteSerializer
from .permissions import PermissaoConsulta
from rest_framework.permissions import IsAuthenticated

class ConsultaViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        usuario = self.request.user
        if usuario.papel == 'medico':   
            return Consulta.objects.filter(medico=usuario)
        else:
            return Consulta.objects.filter(paciente=usuario)
    def get_serializer_class(self):
        paciente = self.request.user
        if paciente.papel =='paciente':
            return ConsultaPacienteSerializer
        else:
            return ConsultaSerializer
    


    permission_classes = [IsAuthenticated, PermissaoConsulta]