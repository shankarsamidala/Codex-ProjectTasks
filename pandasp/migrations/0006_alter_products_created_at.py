# Generated by Django 3.2 on 2023-11-02 03:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandasp', '0005_auto_20231102_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 2, 8, 38, 44, 812155)),
        ),
    ]
