# Generated by Django 4.2.7 on 2023-11-07 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='mobiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('price', models.CharField(max_length=220)),
                ('tag', models.CharField(max_length=220)),
            ],
        ),
    ]
