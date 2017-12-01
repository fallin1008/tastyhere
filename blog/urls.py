from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^mapspage.html$', views.mapspage, name='mapspage'),
    url(r'^aboutus.html$', views.aboutus, name='aboutus'),
    url(r'^contactus.html$', views.contactus, name='contactus'),
    url(r'^intro.gif$', views.intro, name='intro'),
]