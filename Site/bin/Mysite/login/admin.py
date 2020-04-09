from __future__ import unicode_literals
from django.contrib import admin
from . import models

@admin.register(models.Logindb)
class loginadmin(admin.ModelAdmin):
    model = models.Logindb
