from rest_framework import permissions


class AuthorModifyOrReadOnly(permissions.IsAuthenticatedOrReadOnly):
    """
    Usuario no autenticado → puede ver la lista de posts, pero no crear ni modificar.
    Usuario autenticado → puede crear posts.
    Usuario autenticado que no es el autor → puede leer posts ajenos, pero no modificarlos ni borrarlos.
    Usuario autenticado que sí es el autor → puede modificar o borrar sus propios posts.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return request.user == obj.author


class IsAdminUserForObject(permissions.IsAdminUser):
    def has_object_permission(self, request, view, obj):
        return bool(request.user and request.user.is_staff)