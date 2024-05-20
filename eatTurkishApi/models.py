from django.db import models


# Create your models here.
class PopularDishes(models.Model):
    img = models.URLField()
    title = models.CharField(max_length=70)
    price = models.FloatField()
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)
    like = models.PositiveBigIntegerField(default=0)

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


class Testimony(models.Model):
    name = models.CharField(max_length=60)
    comment = models.CharField(max_length=2000)
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    views = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name_plural = 'Testimonies'
        ordering = ['last_update']
        verbose_name = 'Testimony'
        db_table = 'testimony'


class News(models.Model):
    img = models.URLField()
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=160)
    text = models.TextField()
    last_update = models.DateField(auto_now=True)
    create_date = models.DateField(auto_now_add=True)
    views = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-last_update']
        verbose_name = 'News'
        db_table = 'news'


class AboutUs(models.Model):
    text1 = models.TextField()
    img = models.URLField()
    text2 = models.TextField()


class SendMessage(models.Model):
    name = models.CharField(max_length=70)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=20)
    message = models.TextField()
