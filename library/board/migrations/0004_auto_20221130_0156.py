# Generated by Django 3.0.7 on 2022-11-30 01:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_auto_20221130_0115'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newsboard',
            options={'ordering': ['news_date', 'news_title', 'news_date']},
        ),
        migrations.AlterField(
            model_name='newsboard',
            name='news_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
