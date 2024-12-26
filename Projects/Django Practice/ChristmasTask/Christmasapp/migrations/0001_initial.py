# Generated by Django 5.1.4 on 2024-12-25 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Santa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.BigIntegerField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=10)),
            ],
        ),
    ]
