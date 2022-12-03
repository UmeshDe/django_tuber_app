# Generated by Django 4.1.3 on 2022-11-20 11:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hiretuber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('tuber_id', models.IntegerField(blank=True, max_length=255)),
                ('tuber_name', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('message', models.TextField(max_length=255)),
                ('user_id', models.IntegerField(blank=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
