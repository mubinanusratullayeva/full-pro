# Generated by Django 5.0.6 on 2024-05-19 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eatTurkishApi', '0006_alter_populardishes_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text1', models.TextField()),
                ('img', models.URLField()),
                ('text2', models.TextField()),
            ],
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-last_update'], 'verbose_name': 'News', 'verbose_name_plural': 'News'},
        ),
    ]