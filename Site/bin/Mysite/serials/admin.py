from __future__ import unicode_literals
from django.contrib import admin
from . import models

@admin.register(models.Serials)
class serialadmin(admin.ModelAdmin):
    model = models.Serials
