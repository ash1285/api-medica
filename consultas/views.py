from rest_framework import viewsets
from .models import Consulta
from .serializers import ConsultaSerializer
from .permissions import PermissaoConsulta
from rest_framework.permissions import IsAuthenticated

class ConsultaViewSet(viewsets.ModelViewSet):
    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [IsAuthenticated, PermissaoConsulta]