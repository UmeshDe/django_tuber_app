# Generated by Django 4.1.3 on 2022-12-01 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='company_name',
            field=models.CharField(default='NA', max_length=255),
            preserve_default=False,
        ),
    ]
