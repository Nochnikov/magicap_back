# Generated by Django 5.0.6 on 2024-07-01 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0003_facility_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facility',
            name='user',
        ),
    ]