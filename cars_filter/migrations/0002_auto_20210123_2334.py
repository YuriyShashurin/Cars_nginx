# Generated by Django 3.1.5 on 2021-01-23 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_filter', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='year_create',
            field=models.IntegerField(),
        ),
    ]