# Generated by Django 3.0.5 on 2020-04-24 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0027_auto_20200424_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='time',
            field=models.DurationField(),
        ),
    ]
