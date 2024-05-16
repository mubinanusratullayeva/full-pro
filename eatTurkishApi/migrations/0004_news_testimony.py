# Generated by Django 5.0.6 on 2024-05-16 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatTurkishApi', '0003_menupackages'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.URLField()),
                ('title', models.CharField(max_length=70)),
                ('description', models.CharField(max_length=160)),
                ('text', models.TextField()),
                ('last_update', models.DateField(auto_now=True)),
                ('create_date', models.DateField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
                'db_table': 'news',
                'ordering': ['last_update'],
            },
        ),
        migrations.CreateModel(
            name='Testimony',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('comment', models.CharField(max_length=2000)),
                ('last_update', models.DateField(auto_now=True)),
                ('create_date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField(auto_now_add=True)),
                ('views', models.PositiveBigIntegerField()),
            ],
            options={
                'verbose_name': 'Testimony',
                'verbose_name_plural': 'Testimonies',
                'db_table': 'testimony',
                'ordering': ['last_update'],
            },
        ),
    ]
