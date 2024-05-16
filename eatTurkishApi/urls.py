from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PopularDishesAPI, MenuPackagesAPI, TestimonyAPI, NewsAPI


routers = DefaultRouter()

routers.register('popular-dishes', viewset=PopularDishesAPI)
routers.register('menu-packages', viewset=MenuPackagesAPI)
routers.register('testimony', viewset=TestimonyAPI)
routers.register('news', viewset=NewsAPI)


urlpatterns = [
    path('', include(routers.urls)),
]
