# Generated by Django 3.2.3 on 2021-09-06 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('green', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='green',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Наличие'),
        ),
        migrations.AddField(
            model_name='green',
            name='price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=9, verbose_name='Цена'),
        ),
    ]
