# Generated by Django 3.1 on 2020-08-29 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('price_check_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='search',
            name='created',
        ),
    ]
