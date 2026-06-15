from rest_framework import permissions

class IsAdministrador(permissions.BasePermission):
    """Permissão para usuários do tipo ADMINISTRADOR"""
    
    def has_permission(self, request, view):
        return (
            request.user and 
            request.user.is_authenticated and 
            request.user.tipo_usuario == 'ADMINISTRADOR'
        )


class IsAdministradorOrModerador(permissions.BasePermission):
    """Permissão para ADMINISTRADOR ou MODERADOR"""
    
    def has_permission(self, request, view):
        return (
            request.user and 
            request.user.is_authenticated and 
            request.user.tipo_usuario in ['ADMINISTRADOR', 'MODERADOR']
        )


class IsModerador(permissions.BasePermission):
    """Permissão para usuários do tipo MODERADOR"""
    
    def has_permission(self, request, view):
        return (
            request.user and 
            request.user.is_authenticated and 
            request.user.tipo_usuario == 'MODERADOR'
        )


class IsParceiro(permissions.BasePermission):
    """Permissão para usuários do tipo PARCEIRO"""
    
    def has_permission(self, request, view):
        return (
            request.user and 
            request.user.is_authenticated and 
            request.user.tipo_usuario == 'PARCEIRO'
        )


class IsRudiero(permissions.BasePermission):
    """Permissão para usuários do tipo RUDIERO"""
    
    def has_permission(self, request, view):
        return (
            request.user and 
            request.user.is_authenticated and 
            request.user.tipo_usuario == 'RUDIERO'
        )