# Generated by Django 3.2 on 2022-12-14 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='borrowBook',
        ),
    ]
