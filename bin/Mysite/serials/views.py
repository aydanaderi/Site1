from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.utils.crypto import get_random_string
from django.core import serializers
from datetime import datetime
from . import models
import json

def serialsViewes(request):
    year = datetime.now().year
    month = datetime.now().month
    year = year % 1000
    year1 = str(year / 10)
    year2 = str(year % 10)
    if month <= 9 :
        month = str(month % 10)
    elif month == 10 :
        month = "A"
    elif month == 11 :
        month = "B"
    else :
        month = "C"
    random_char1 = get_random_string(length = 1,allowed_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')
    random_char2 = get_random_string(length = 1,allowed_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')
    random_char3 = get_random_string(length = 1,allowed_chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890')
    arryserial = "T" + "1" + year1 + year2 + month + "0" + "0" + random_char1 + random_char2 + random_char3
    return HttpResponse(arryserial)

def insertserials(request):
    srl = serialsViewes(request)
    srl = str(','.join(srl))
                                                                                                 #data base
    if models.Serials.objects.filter(serial = srl):
        insert = models.Serials.objects.all()
    else :
        insert = models.Serials.objects.all()
        insert = models.Serials.objects.create(serial = srl,date = datetime.now())
        insert.save()
    list = []
    for s in models.Serials.objects.all():
        list.append(s.id)
        list.append(s.serial)
        list.append(s.date)
    return JsonResponse(list ,safe = False)
                                                                                                #end
