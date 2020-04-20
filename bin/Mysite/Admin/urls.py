from django.conf.urls import url
from . import views

app_name = 'admin'
urlpatterns = [
    url(r'^loginadmin/$', views.LoginAdminView,name = 'LoginAdminView'),
    url(r'^homeadmin/$', views.HomeAdminView,name = 'HomeAdminView'),
]
