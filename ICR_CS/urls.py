from django.conf.urls import url, include
from ICR_CS.views import index
from . import views

urlpatterns = [
	url(r'^result/(?P<idImagen>\d+)/$', views.mostrar_resultado, name='resultado'),
	url(r'^$', index, name='index'),
]
