# Generated by Django 4.1.3 on 2022-11-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='link',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
