# Generated by Django 3.2 on 2023-11-01 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pandasp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
