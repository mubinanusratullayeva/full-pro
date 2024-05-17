from django.shortcuts import render
from django.db import transaction

from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.decorators import action

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

    @transaction.atomic
    @action(detail=True, methods=['GET'])
    def views(self, request, *args, **kwargs):
        testimony = self.get_object()
        testimony.views += 1
        testimony.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class NewsAPI(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
