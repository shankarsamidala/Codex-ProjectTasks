# Generated by Django 3.2 on 2023-11-01 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='productList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('tag', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('rating', models.IntegerField()),
            ],
        ),
    ]
