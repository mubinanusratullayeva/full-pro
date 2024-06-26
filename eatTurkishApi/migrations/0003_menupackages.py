# Generated by Django 5.0.6 on 2024-05-16 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatTurkishApi', '0002_rename_populardish_populardishes'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuPackages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.URLField()),
                ('title', models.CharField(max_length=70)),
                ('price', models.IntegerField()),
                ('last_update', models.DateField(auto_now=True)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Menu Package',
                'verbose_name_plural': 'Menu packages',
                'db_table': 'menu_packages',
                'ordering': ['title'],
            },
        ),
    ]
