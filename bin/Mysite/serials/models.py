from __future__ import unicode_literals
from django.db import models
from datetime import datetime

class Serials (models.Model):
    serial = models.CharField(max_length = 10)
    id = models.AutoField(primary_key = True)
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.serial
