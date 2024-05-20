from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponse

from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action

from .models import PopularDishes, MenuPackages, Testimony, News, AboutUs, SendMessage
from .serializers import PopularDishesSerializer, MenuPackagesSerializer, TestimonySerializer, NewsSerializer, AboutUsSerializer, SendMessageSerializer


# Create your views here.
class PopularDishesAPI(ModelViewSet):
    queryset = PopularDishes.objects.all()
    serializer_class = PopularDishesSerializer


class MenuPackagesAPI(ModelViewSet):
    queryset = MenuPackages.objects.all()
    serializer_class = MenuPackagesSerializer


class TestimonyAPI(ModelViewSet):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer

    @transaction.atomic
    @action(detail=True, methods=['GET'])
    def views(self, request, *args, **kwargs):
        testimony = self.get_object()
        testimony.views += 1
        testimony.save()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class NewsAPI(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class AboutUsAPI(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class SendMessageAPI(ModelViewSet):
    queryset = SendMessage.objects.all()
    serializer_class = SendMessageSerializer
