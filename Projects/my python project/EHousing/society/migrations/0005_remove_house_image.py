# Generated by Django 5.1.6 on 2025-02-24 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('society', '0004_house_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='house',
            name='image',
        ),
    ]
