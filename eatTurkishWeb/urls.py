from django.urls import path

from .views import HomePageView, UserRegistrationView, UserLoginView, UserLogOutView, NewsDetailView, NewsView, ContactUsView, AboutUsView


urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/<int:id>/', NewsDetailView.as_view(), name='news_detail'),
    path('contact-us/', ContactUsView.as_view(), name='contact-us'),
    path('about-us/', AboutUsView.as_view(), name='about-us'),
    path('auth/login/', UserLoginView.as_view(), name='login'),
    path('auth/register/', UserRegistrationView.as_view(), name='register'),
    path('auth/logout/', UserLogOutView.as_view(), name='logout'),
]
