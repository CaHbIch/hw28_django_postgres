from rest_framework import viewsets

from users.models.location import Location
from users.models.user import User
from users.serializers import UserSerializer, LocationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ Для списка пользователей """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class LocationViewSet(viewsets.ModelViewSet):
    """ Для списка локаций """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
