from rest_framework import serializers

from .models import PopularDishes, MenuPackages, Testimony, News


class PopularDishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularDishes
        fields = ('img', 'title', 'price', )


class MenuPackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPackages
        fields = ('img', 'title', 'price', )


class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimony
        fields = ('name', 'comment', 'last_update', 'time', 'views', )


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('img', 'title', 'description', 'text', )
