# Generated by Django 4.1.2 on 2022-11-13 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_alter_car_price'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='car',
            index=models.Index(fields=['name', 'mileage', 'price', 'dealer_name', 'carURL'], name='store_car_name_8b93ff_idx'),
        ),
        migrations.AlterModelTable(
            name='car',
            table='store_car',
        ),
    ]
