# Generated by Django 3.0.5 on 2020-04-19 11:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0011_auto_20200418_1311'),
    ]

    operations = [
        migrations.AddField(
            model_name='logindb',
            name='email',
            field=models.EmailField(default='ayda.f.naderi@gmail.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='logindb',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 11, 39, 59, 530666)),
        ),
        migrations.AlterField(
            model_name='logindb',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 19, 11, 39, 59, 530690)),
        ),
    ]