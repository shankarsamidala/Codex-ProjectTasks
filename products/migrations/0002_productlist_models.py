# Generated by Django 3.2 on 2023-11-02 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='productlist',
            name='models',
            field=models.CharField(default=22, max_length=250),
            preserve_default=False,
        ),
    ]
