# Generated by Django 3.2 on 2022-12-09 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_author_intro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='intro',
            field=models.TextField(blank=True, help_text='저자 소개를 작성해 주세요', max_length=1000, null=True),
        ),
    ]
