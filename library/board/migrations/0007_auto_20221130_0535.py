# Generated by Django 3.0.7 on 2022-11-30 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_auto_20221130_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsboard',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
