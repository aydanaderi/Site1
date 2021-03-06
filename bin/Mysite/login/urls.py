from django.conf.urls import url
from login import views

app_name = 'sigup'
urlpatterns = [
    url(r'^signup/$', views.SignupView, name = 'SignupView'),
    url(r'^login/$', views.LoginView, name = 'LoginView'),
    url(r'^home/$', views.HomeView, name = 'HomeView'),
    url(r'^user/$', views.UserView, name = 'UserView'),
    url(r'basic/$', views.BasicView, name = 'BasicView'),
    url(r'upload/$', views.UploadView, name = 'UploadView'),
]
