from rest_framework import serializers

from ads.models.ad import Ad
from ads.models.category import Category
from user.models.location import Location


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'


class CatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class LocSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'
