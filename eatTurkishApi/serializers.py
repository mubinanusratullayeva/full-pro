from rest_framework import serializers

from .models import PopularDishes, MenuPackages, Testimony, News, AboutUs, SendMessage


class PopularDishesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PopularDishes
        fields = ('img', 'title', 'price',)


class MenuPackagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuPackages
        fields = ('img', 'title', 'price',)


class TestimonySerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimony
        fields = ('name', 'comment', 'last_update', 'time', 'views',)


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('img', 'title', 'description', 'text',)


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ('text1', 'img', 'text2', )


class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SendMessage
        fields = ('name', 'email', 'phone', 'message', )
