from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^$', views.home, name='home'),
    url(r'^happy/', views.happy, name='happy'),
    url(r'^sad/', views.sad, name='sad'),
    url(r'^mad/', views.mad, name='mad'),
    url(r'^angry/', views.angry, name='angry'),
    url(r'^fearfull/', views.fearfull, name='fearfull'),
    url(r'^disgusted/', views.disgusted, name='disgusted'),
    url(r'^surprised/', views.surprised, name='surprised'),
    url(r'^blog/', views.wheel, name='wheel'),
    url(r'^start/$', views.start, name='start'),
]
