from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User

import requests


# Create your views here.
class HomePageView(View):
    def get_data(self, param):
        BASE_URL = f"http://127.0.0.1:8000/api/v1/{param}/"
        response = requests.get(BASE_URL)
        data = response.json()
        return data

    def get(self, request):
        context = {
            'popular_dishes': self.get_data('popular-dishes'),
            'testimonies': self.get_data('testimony'),
            'news': self.get_data('news'),
        }
        return render(request, 'pages/home.html', context)


class NewsView(View):
    def get_data(self):
        BASE_URL = f"http://127.0.0.1:8000/api/v1/news/"
        response = requests.get(BASE_URL)
        data = response.json()
        return data
    
    def get(self, request):
        context = {
            'news': self.get_data(),
        }
        return render(request, 'pages/news.html', context)


class NewsDetailView(View):
    def get(self,request, id):
        BASE_URL = f"http://127.0.0.1:8000/api/v1/news/{id}/"
        response = requests.get(url=BASE_URL)
        news_detail = response.json()
        context = {'news_detail': news_detail}
        return redirect(request, 'pages/news_detail.html', context)


class UserRegistrationView(View):
    def get(self, request):
        return render(request, 'auth/register.html')
    
    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password_conf = request.POST['password_conf']

        user = User(first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password)
        user.save()
        return redirect('home')


class UserLoginView(View):
    def get(self, request):
        return render(request, 'auth/login.html')
