# Generated by Django 3.2 on 2023-11-01 12:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
