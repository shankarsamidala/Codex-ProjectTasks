# Generated by Django 3.2 on 2023-11-01 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productlist',
            old_name='title',
            new_name='name',
        ),
    ]
