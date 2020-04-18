from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class Logindb (models.Model) :
    username =  models.BigIntegerField()
    password = models.CharField(max_length = 100)
    date = models.DateTimeField(default = datetime.now())
    time = models.DateTimeField(default = datetime.now())


class Documents(models.Model):
    docfile = models.FileField()
