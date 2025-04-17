from rest_framework.permissions import BasePermission

class BasePaidContentPermission(BasePermission):

    model = None
    limit = 1

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        user = request.user
        if not user.is_authenticated:
            return False

        if user.is_paid:
            return True

        allowed_objects = self.model.objects.order_by('id')[:self.limit]
        return obj in allowed_objects
