# Generated by Django 3.2 on 2023-11-01 16:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandasp', '0002_auto_20231101_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 1, 21, 49, 43, 802324)),
        ),
    ]
