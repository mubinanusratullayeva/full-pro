from django.urls import path

from .views import HomePageView, UserRegistrationView, UserLoginView, NewsDetailView, NewsView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/<int:id>/', NewsDetailView.as_view(), name='newsdetail'),
    path('auth/login/', UserLoginView.as_view(), name='login'),
    path('auth/register/', UserRegistrationView.as_view(), name='register'),
]
