from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^home/$', views.home, name = 'home'),
    url(r'^category/(?P<categoria_id>\d+)/$', views.categoria, name='category'),
    url(r'^product/(?P<producto_id>\d+)/$', views.producto, name='product'),
]