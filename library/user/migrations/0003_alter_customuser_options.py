# Generated by Django 3.2 on 2022-12-14 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_customuser_borrowbook'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['email', 'username']},
        ),
    ]