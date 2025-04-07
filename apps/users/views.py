from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from rest_framework import generics

from apps.users.models import CustomUser, Support
from apps.users.serializers import UserListSerializer, EditProfileSerializer, SupportSerializer
from apps.quizzes.models.question import Question


class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.order_by('-created_at')
    serializer_class = UserListSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['total_questions'] = Question.objects.count()
        return context


class EditProfileAPIView(generics.GenericAPIView):
    serializer_class = EditProfileSerializer
    parser_classes = [MultiPartParser, FormParser]
    def patch(self, request, *args, **kwargs):

        user = request.user
        serializer = self.get_serializer(instance=user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response()


class SupportAPIView(generics.CreateAPIView):
    queryset = Support.objects.order_by('-created_at')
    serializer_class = SupportSerializer




