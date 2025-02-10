# Generated by Django 5.1.5 on 2025-01-31 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_contact_permissionroles'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='signup',
            new_name='Usersignup',
        ),
        migrations.AlterField(
            model_name='permissionroles',
            name='user_type',
            field=models.CharField(choices=[(2, 'doctor'), (3, 'Admin'), (1, 'patients')], default=1, max_length=50),
        ),
    ]
