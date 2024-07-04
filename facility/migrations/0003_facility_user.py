# Generated by Django 5.0.6 on 2024-07-01 11:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0002_category_facility_expired_date_facility_category'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='user',
            field=models.ManyToManyField(related_name='facilities', to=settings.AUTH_USER_MODEL),
        ),
    ]