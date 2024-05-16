from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from .models import PopularDishes, MenuPackages
from .serializers import PopularDishesSerializer, MenuPackagesSerializer


# Create your views here.
class PopularDishesAPI(ModelViewSet):
    queryset = PopularDishes.objects.all()
    serializer_class = PopularDishesSerializer


class MenuPackagesAPI(ModelViewSet):
    queryset = MenuPackages.objects.all()
    serializer_class = MenuPackagesSerializer