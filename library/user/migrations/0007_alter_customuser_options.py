# Generated by Django 3.2 on 2022-12-14 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_customuser_nikname'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['username', 'nikname']},
        ),
    ]