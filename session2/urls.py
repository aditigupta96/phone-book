from django.conf.urls import url
from django.contrib import admin
from crud import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^insert/$', views.insert, name='insert'),
    url(r'^delete/(?P<person_id>\d+)$', views.delete, name='delete'),
    url(r'^edit/(?P<person_id>\d+)$', views.edit, name='edit'),
]
