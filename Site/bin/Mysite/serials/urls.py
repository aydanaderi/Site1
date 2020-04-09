from django.conf.urls import url
from . import views

app_name = 'serials'
urlpatterns = [
    url(r'^$', views.insertserials,name = 'insertserials'),
]
