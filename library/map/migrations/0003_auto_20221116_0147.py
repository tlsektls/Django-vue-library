# Generated by Django 3.0.7 on 2022-11-16 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0002_map_latitude_map_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='mymodelname',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]