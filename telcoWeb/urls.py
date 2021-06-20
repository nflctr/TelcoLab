from django.urls import path
from . import views

urlpatterns = [
  path('', views.telcoLab, name='telcoLab'),
  path('signalGenerator', views.signalGenerator, name='signalGenerator'),
  path('dsbfcModulation', views.dsbfcModulation, name='dsbfcModulation'),
  path('dsbscModulation', views.dsbscModulation, name='dsbscModulation'),
  path('ssbModulation', views.ssbModulation, name='ssbModulation'),
  path('frequencyModulation', views.frequencyModulation, name='frequencyModulation'),
  path('digitalModulation', views.digitalModulation, name='digitalModulation'),    
  path('index', views.index, name='index'),
]
