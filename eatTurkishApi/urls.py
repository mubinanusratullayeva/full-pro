from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import PopularDishesAPI, MenuPackagesAPI, TestimonyAPI, NewsAPI, AboutUsAPI


routers = DefaultRouter()

routers.register('popular-dishes', viewset=PopularDishesAPI)
routers.register('menu-packages', viewset=MenuPackagesAPI)
routers.register('testimony', viewset=TestimonyAPI)
routers.register('news', viewset=NewsAPI)
routers.register('about-us', viewset=AboutUsAPI)


urlpatterns = [
    path('', include(routers.urls)),
]
