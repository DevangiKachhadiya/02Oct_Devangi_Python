# Generated by Django 5.1.5 on 2025-01-31 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_usersignup_lastname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissionroles',
            name='user_type',
            field=models.CharField(choices=[(3, 'Admin'), (2, 'doctor'), (1, 'patients')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='usersignup',
            name='role',
            field=models.CharField(max_length=20),
        ),
    ]
