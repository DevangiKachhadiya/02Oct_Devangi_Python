# Generated by Django 5.1.6 on 2025-02-24 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('society', '0003_remove_house_image_houseimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='image',
            field=models.ImageField(default='default.png', upload_to='house_images/'),
            preserve_default=False,
        ),
    ]
