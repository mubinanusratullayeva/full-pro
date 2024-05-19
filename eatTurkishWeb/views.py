from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin

import requests

from .forms import UserLoginForm

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


class NewsView(LoginRequiredMixin, View):
    def get_data(self):
        BASE_URL = "http://127.0.0.1:8000/api/v1/news/"
        response = requests.get(BASE_URL)
        data = response.json()
        return data
    
    def get(self, request):
        context = {
            'news': self.get_data(),
        }
        return render(request, 'pages/news.html', context)


class NewsDetailView(LoginRequiredMixin, View):
    def get_data(self, id):
        BASE_URL = f"http://127.0.0.1:8000/api/v1/news/{id}/"
        response = requests.get(BASE_URL)
        data = response.json()
        return data
    
    def get(self,request, id):
        context = {'newsDetail': self.get_data(id=id)}
        return render(request, 'pages/news_detail.html', context)
    

class AboutUsView(LoginRequiredMixin, View):
    def get(self, request):
        BASE_URL = f"http://127.0.0.1:8000/api/v1/about-us/"
        response = requests.get(BASE_URL)
        data = response.json()
        context = {'abu': data}
        return render(request, 'pages/about_us.html', context)


class ContactUsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'pages/contact_us.html')


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

        if password_conf == password:
            user = User(first_name=first_name, last_name=last_name, username=username, email=email)
            user.set_password(password)
            user.save()
            return redirect('login')
        else:
            return render(request, 'auth/register.html')


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {
            'form': form,
        }
        return render(request, 'auth/login.html', context)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        data = {
            'username': username,
            'password': password,
        }

        login_form = AuthenticationForm(data=data)
        if login_form.is_valid():
            user = login_form.get_user()
            login(request, user)
            return redirect('home')
        else:
            form = UserLoginForm()
            context = {
                'form': form,
            }
            return render(request, 'auth/login.html', context)

class UserLogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('home')
