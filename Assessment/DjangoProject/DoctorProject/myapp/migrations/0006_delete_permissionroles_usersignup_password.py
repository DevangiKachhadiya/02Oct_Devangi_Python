# Generated by Django 5.1.5 on 2025-01-31 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_alter_permissionroles_user_type_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='permissionroles',
        ),
        migrations.AddField(
            model_name='usersignup',
            name='password',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
    ]
