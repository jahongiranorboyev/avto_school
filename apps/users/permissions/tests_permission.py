from rest_framework.permissions import BasePermission

class CanAccessQuestions(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        if user.is_authenticated and user.is_paid:
            return True
        return False