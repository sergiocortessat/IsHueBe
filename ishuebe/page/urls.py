from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog/', views.wheel, name='wheel'),
    url(r'^contact/$', views.contact, name='contact'),
]
