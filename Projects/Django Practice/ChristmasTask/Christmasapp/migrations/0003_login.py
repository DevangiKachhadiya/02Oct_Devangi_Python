# Generated by Django 5.1.4 on 2024-12-26 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Christmasapp', '0002_alter_santa_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=10)),
            ],
        ),
    ]
