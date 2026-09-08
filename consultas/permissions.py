from rest_framework import permissions


class PermissaoConsulta(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'POST':
            return request.user.papel == 'medico'
        return True

    def has_object_permission(self, request, view, obj):
        return request.user == obj.medico or request.user == obj.paciente