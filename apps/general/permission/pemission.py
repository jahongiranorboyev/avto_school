from rest_framework import permissions
from rest_framework.permissions import BasePermission


class LevelPermission(BasePermission):
    def has_permission(self, request, view):
        pass