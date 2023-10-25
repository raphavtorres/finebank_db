from rest_framework import permissions


class SuperUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False


class CustomerGetPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return get_customer_permission(request, 'GET')


class CustomerPostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return get_customer_permission(request, 'POST')


class CustomerGetPostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return get_customer_permission(request, 'GET POST')


class CustomerGetPostPatchPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return get_customer_permission(request, 'GET POST PUT PATCH')


class DeletePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "DELETE":
            if request.user.is_is_superuser:
                return True
            return False
        return True


def get_customer_permission(request, methods):
    if request.user.is_superuser:
        return True

    if request.method in methods:
        if request.user.is_authenticated:
            return True
        return False
    return False
