from rest_framework.serializers import ModelSerializer

from .models import User


class UserModelSerializer(ModelSerializer):
    """ Сериалайзер создания поьльзователя """
    class Meta:
        model = User
        fields = "__all__"
