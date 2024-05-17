from django.contrib import admin

from .models import PopularDishes, News, MenuPackages, Testimony


# Register your models here.
admin.site.register(PopularDishes)
admin.site.register(MenuPackages)
admin.site.register(Testimony)
admin.site.register(News)
