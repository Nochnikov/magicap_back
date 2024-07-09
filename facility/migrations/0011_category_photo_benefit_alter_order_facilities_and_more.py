# Generated by Django 5.0.6 on 2024-07-09 13:55

import django.db.models.deletion
import facility.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facility', '0010_alter_order_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='categories/'),
        ),
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('expired_date', models.DateField(default=facility.models.get_expired_date)),
                ('cost', models.PositiveIntegerField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='benefits/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facility.category')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='facilities',
            field=models.ManyToManyField(to='facility.benefit'),
        ),
        migrations.DeleteModel(
            name='Facility',
        ),
    ]