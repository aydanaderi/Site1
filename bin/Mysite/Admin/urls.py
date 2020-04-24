from django.conf.urls import url
from . import views

app_name = 'admin'
urlpatterns = [
    url(r'^Admin/$', views.LoginAdminView,name = 'LoginAdminView'),
    url(r'^Home/$', views.HomeAdminView,name = 'HomeAdminView'),
    url(r'^Informations/$', views.InformationsView,name = 'InformationsView'),
    url(r'^Serials/$', views.SerialsView,name = 'SerialsView'),
]
