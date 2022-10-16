from django.db.models import Count, Q
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

from ads.models.ad import Ad
from ads.models.category import Category
from users.models.location import Location
from users.models.user import User
from users.serializers import UserSerializer, LocationSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ Для списка пользователей """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)
    q = User.objects.values("ad__is_published").annotate(total_ads=Count('username'))


class LocationViewSet(viewsets.ModelViewSet):
    """ Для списка локаций """
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
