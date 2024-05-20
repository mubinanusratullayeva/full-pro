from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponse

from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from django_filters import rest_framework as filters
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import PopularDishes, MenuPackages, Testimony, News, AboutUs, SendMessage
from .serializers import PopularDishesSerializer, MenuPackagesSerializer, TestimonySerializer, NewsSerializer, AboutUsSerializer, SendMessageSerializer


# Create your views here.
class PopularDishesAPI(ModelViewSet):
    queryset = PopularDishes.objects.all()
    serializer_class = PopularDishesSerializer

    @action(detail=True, methods=['POST'])
    def like(self, request, *args, **kwargs):
        dishes = self.get_object()
        dishes.like += 1
        dishes.save()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(detail=False, methods=['POST'])
    def top(self, request, *args, **kwargs):
        dishes = self.get_queryset()
        dishes = dishes.order_by('-like')[:5]
        serializer = PopularDishesSerializer(dishes, many=True)
        return Response(data=serializer.data)


class MenuPackagesAPI(ModelViewSet):
    queryset = MenuPackages.objects.all()
    serializer_class = MenuPackagesSerializer


class TestimonyAPI(ModelViewSet):
    queryset = Testimony.objects.all()
    serializer_class = TestimonySerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'last_update', 'views', )

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
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('title', 'last_update', )

    @transaction.atomic
    @action(detail=True, methods=['GET'])
    def views(self, request, *args, **kwargs):
        news = self.get_object()
        news.views += 1
        news.save()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class AboutUsAPI(ModelViewSet):
    queryset = AboutUs.objects.all()
    serializer_class = AboutUsSerializer


class SendMessageAPI(ModelViewSet):
    queryset = SendMessage.objects.all()
    serializer_class = SendMessageSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ('name', 'email', 'phone', )