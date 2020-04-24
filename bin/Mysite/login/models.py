from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class Information(models.Model) :
    username =  models.BigIntegerField()
    password = models.CharField(max_length = 100)
    date = models.DateTimeField()
    time = models.CharField(max_length = 500)
    email = models.EmailField(max_length = 254)
    profile = models.FileField()
