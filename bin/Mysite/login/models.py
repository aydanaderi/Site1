from __future__ import unicode_literals
from django.db import models

class Logindb (models.Model) :
    username =  models.BigIntegerField()
    password = models.CharField(max_length = 100)
