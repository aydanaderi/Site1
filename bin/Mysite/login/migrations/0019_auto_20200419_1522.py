# Generated by Django 3.0.5 on 2020-04-19 15:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0018_auto_20200419_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 15, 22, 26, 920302)),
        ),
        migrations.AlterField(
            model_name='information',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 15, 22, 26, 920326)),
        ),
    ]
