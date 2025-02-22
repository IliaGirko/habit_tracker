from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt import views

from .models import User
from .serializers import UserModelSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ Вьювсет пользователя """
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(self.request.data.get("password"))
        user.save()


class UserTokenObtainPairView(views.TokenObtainPairView):
    """ Вьюшка создания токена """
    permission_classes = [AllowAny]


class UserTokenRefreshView(views.TokenRefreshView):
    """ Вьюшка рефреша токена """
    permission_classes = [AllowAny]
