# Generated by Django 5.1.5 on 2025-02-03 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_remove_doctor_user_remove_patient_user_doctor_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='Contact',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Contact',
            field=models.BigIntegerField(),
        ),
    ]
