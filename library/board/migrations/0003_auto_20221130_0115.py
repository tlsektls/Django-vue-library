# Generated by Django 3.0.7 on 2022-11-30 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_auto_20221130_0102'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsboard',
            name='news_poster',
            field=models.ImageField(blank=True, null=True, upload_to='newsborad/'),
        ),
    ]
