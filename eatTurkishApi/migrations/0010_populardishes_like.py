# Generated by Django 5.0.6 on 2024-05-20 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatTurkishApi', '0009_news_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='populardishes',
            name='like',
            field=models.PositiveBigIntegerField(default=0),
        ),
    ]