from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PopularDishesAPI, MenuPackagesAPI


routers = DefaultRouter()

routers.register('popular-dishes', viewset=PopularDishesAPI)
routers.register('menu-packages', viewset=MenuPackagesAPI)


urlpatterns = [
    path('', include(routers.urls)),
]
