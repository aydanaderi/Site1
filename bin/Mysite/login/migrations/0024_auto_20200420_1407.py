# Generated by Django 3.0.5 on 2020-04-20 14:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0023_auto_20200420_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 14, 7, 24, 209064)),
        ),
        migrations.AlterField(
            model_name='information',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 20, 14, 7, 24, 209090)),
        ),
    ]