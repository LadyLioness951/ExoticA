# Generated by Django 3.2.4 on 2021-07-19 01:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='animal',
            name='common_name',
        ),
    ]