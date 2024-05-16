from django.db import models


# Create your models here.
class PopularDishes(models.Model):
    img = models.URLField()
    title = models.CharField(max_length=70)
    price = models.IntegerField()
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = 'Popular dishes'
        ordering = ['title']
        verbose_name = 'Popular dish'
        db_table = 'popular_dishes'


class MenuPackages(models.Model):
    img = models.URLField()
    title = models.CharField(max_length=70)
    price = models.IntegerField()
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = 'Menu packages'
        ordering = ['title']
        verbose_name = 'Menu Package'
        db_table = 'menu_packages'