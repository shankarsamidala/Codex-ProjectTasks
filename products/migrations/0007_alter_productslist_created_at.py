# Generated by Django 3.2 on 2023-11-03 04:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_productslist_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productslist',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 3, 10, 9, 1, 869920)),
        ),
    ]
