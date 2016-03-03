from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', views.index, name='index'),
    url(r'^fade$', views.ejemplos_fade, name='fade'),
    url(r'^slide$', views.ejemplos_slide, name='slide'),
    url(r'^animate$', views.ejemplos_animate, name='animate'),
    url(r'^stop$', views.ejemplos_stop, name='stop'),
    url(r'^cadena$', views.ejemplos_cadena, name='cadena'),
]
