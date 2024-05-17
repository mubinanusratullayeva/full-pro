from django.urls import path

from .views import LandingPageView, HomePageView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
]
