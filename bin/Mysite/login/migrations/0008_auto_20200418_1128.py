# Generated by Django 3.0.5 on 2020-04-18 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0007_auto_20200416_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='logindb',
            name='date',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='logindb',
            name='time',
            field=models.DateTimeField(default=None),
        ),
    ]
