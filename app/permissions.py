from rest_framework import permissions


class SuperUserPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False


class CustomerGetPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return customer_get_permission(request, 'GET')


class CustomerPostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return customer_get_permission(request, 'POST')


class CustomerGetPostPatch(permissions.BasePermission):
    def has_permission(self, request, view):
        return customer_get_permission(request, 'GET POST PUT PATCH')
        # if request.user.is_superuser:
        #     return True

        # if request.method in 'GET POST PUT':
        #     if request.user.is_authenticated:
        #         return True
        #     return False
        # return False


class DeletePermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "DELETE":
            if request.user.is_is_superuser:
                return True
            return False
        return True


def customer_get_permission(request, methods):
    if request.user.is_superuser:
        return True

    if request.method in methods:
        if request.user.is_authenticated:
            return True
        return False
    return False
