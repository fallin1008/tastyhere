from django.conf.urls import include, url
from django.contrib import admin
from blog import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('blog.urls')),

    url(r'^intro.gif/', views.intro),
    url(r'', include('blog.urls')),

    url(r'^mapspage.html', views.mapspage),
    url(r'', include('blog.urls')),

    url(r'^aboutus.html', views.aboutus),
    url(r'', include('blog.urls')),

    url(r'^contactus.html', views.contactus),
    url(r'', include('blog.urls')),

    url(r'^post_list.html', views.post_list),
    url(r'', include('blog.urls')),
]
