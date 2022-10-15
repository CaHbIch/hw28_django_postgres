from rest_framework import generics

from ads.models.ad import Ad
from ads.models.category import Category
from ads.serializers import AdSerializer, CatSerializer

from django.http import JsonResponse


def index(request):
    response = {'status': 'ok'}
    return JsonResponse(response, status=200)


class AdsAPIList(generics.ListCreateAPIView):
    """ Получение всех постов (GET), и создание списка (POST) """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdAPIUpdate(generics.RetrieveUpdateAPIView):
    """ Чтение и изменение поста отдельной записи (GET - и POST - запросы) """
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class CatsAPIList(generics.ListCreateAPIView):
    """ Получение всех категорий (GET), и создание списка (POST) """
    queryset = Category.objects.all()
    serializer_class = CatSerializer


class CatAPIUpdate(generics.RetrieveUpdateAPIView):
    """ Получение одной категорий (GET), и создание списка (POST) """
    queryset = Category.objects.all()
    serializer_class = CatSerializer
