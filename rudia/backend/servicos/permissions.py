from rest_framework import permissions


class IsParceiroOrReadOnly(permissions.BasePermission):
    """
    Permissão que permite leitura para qualquer usuário,
    mas escrita apenas para usuários do tipo PARCEIRO
    """
    
    def has_permission(self, request, view):
        # Métodos seguros (GET, HEAD, OPTIONS) são permitidos para todos
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Métodos de escrita (POST, PUT, PATCH, DELETE) apenas para PARCEIRO autenticado
        return (
            request.user and 
            request.user.is_authenticated and 
            request.user.tipo_usuario == 'PARCEIRO'
        )
