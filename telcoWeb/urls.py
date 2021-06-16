from os import name
from django.urls import path
from . import views

urlpatterns = [
  path('', views.coba, name='coba'),
  path('generator', views.generator, name='generator'),
  path('dsbfc', views.dsbfc, name='dsbfc'),
  path('dsbsc', views.dsbsc, name='dsbsc'),
  path('ssb', views.ssb, name='ssb'),
  path('fm', views.fm, name='fm'),
  path('digital', views.digital, name='digital'),    
  path('index', views.index, name='index'),
]
