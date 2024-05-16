from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import PopularDishes, MenuPackages, Testimony, News
from .serializers import PopularDishesSerializer, MenuPackagesSerializer, TestimonySerializer, NewsSerializer


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


class NewsAPI(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
