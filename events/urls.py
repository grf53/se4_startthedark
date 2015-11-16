from django.conf.urls import include, url
from events import views

urlpatterns = [
    url(r'^create/$', views.create, name='ev_create'),
    url(r'^tonight/$', views.tonight, name='ev_tonight'),
]
