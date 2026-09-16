from rest_framework import permissions


class PermissaoConsulta(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.papel == 'medico'
        return True

    def has_object_permission(self, request, view, obj):
        if request.user == obj.medico: 
            return True
        if request.user == obj.paciente and request.method in ['GET', 'PATCH']:
            return True
        return False
            
   