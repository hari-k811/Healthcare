# Generated by Django 5.0.3 on 2024-04-12 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('health', '0003_remove_doctor_password_remove_doctor_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='address',
            field=models.CharField(max_length=40),
        ),
    ]
