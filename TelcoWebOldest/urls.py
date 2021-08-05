from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('base', views.base, name='base'),
    path('experiments', views.experiments, name='experiments'),
    path('external', views.external, name='external'),
    path('signal', views.signal, name='signal')
]