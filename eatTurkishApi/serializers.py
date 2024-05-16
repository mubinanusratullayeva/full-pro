from rest_framework import serializers

from .models import PopularDishes, MenuPackages


class PopularDishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularDishes
        fields = ('img', 'title', 'price', )


class MenuPackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPackages
        fields = ('img', 'title', 'price', )
