from django.conf.urls import url
from django.contrib import admin

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # Efectos:
    url(r'^$', views.index, name='index'),
    url(r'^fade$', views.ejemplos_fade, name='fade'),
    url(r'^slide$', views.ejemplos_slide, name='slide'),
    url(r'^animate$', views.ejemplos_animate, name='animate'),
    url(r'^stop$', views.ejemplos_stop, name='stop'),
    url(r'^cadena$', views.ejemplos_cadena, name='cadena'),
    # Juego con el DOM:
    url(r'^set$', views.ejemplos_set, name='set'),
    url(r'^add$', views.ejemplos_add, name='add'),
    # Manipular CSS:
    url(r'^man-css/$', views.manipular_css, name='m-css'),
    url(r'^man-css-II/$', views.manipular_css_II, name='m-css-II'),
    # Dimension:
    url(r'^dim/wid-hei/$', views.dim_wid_hei, name='dim-1'),
    url(r'^dim/innwid-innhei/$', views.dim_innwid_innhei, name='dim-2'),
    # Parent:
    url(r'^parent$', views.parent, name='parent'),
    # Upload:
    url(r'^upload-basico$', views.upload_basico, name='upload_basico'),
]
