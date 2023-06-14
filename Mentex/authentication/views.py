from rest_framework import generics, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView


class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        user = request.user
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')

        # Check if new_password is empty
        if not new_password:
            return Response({'detail': 'New password cannot be empty.'}, status=400)

        if not user.check_password(current_password):
            return Response({'detail': 'Current password is incorrect.'}, status=400)

        user.set_password(new_password)
        user.save()

        return Response({'detail': 'Password has been changed successfully.'}, status=200)


class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
