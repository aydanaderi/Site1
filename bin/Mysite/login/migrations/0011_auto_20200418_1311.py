# Generated by Django 3.0.5 on 2020-04-18 13:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0010_auto_20200418_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='logindb',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 18, 13, 11, 25, 172821)),
        ),
        migrations.AddField(
            model_name='logindb',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 18, 13, 11, 25, 172845)),
        ),
    ]