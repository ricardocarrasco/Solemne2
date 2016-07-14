from django.conf.urls import include, url
from . import views

urlpatterns = [

    url(r'^index/$', views.index, name = 'idex'),
    url(r'^category/(?P<categoria_id>\d+)/$', views.category, name='category'),
    url(r'^product/(?P<producto_id>\d+)/$', views.product, name='product'),
]