# from django.contrib import admin
from django.urls import path
from TelcoWebOlder import views

urlpatterns = [

    # TelcoLAB versi baru
    path('', views.coba, name='coba'),

    # TelcoLAB versi awal
    path('home', views.home, name='home'),
    path('base', views.base, name='base'),
    path('experiments', views.experiments, name='experiments'),
    
    # Path ke eksperimen
    path('index', views.index, name='index'),
    path('test', views.test, name='test'),
    path('signalgen', views.signalgen, name='signalgen'),
    path('am', views.am, name='am'),
    path('fm', views.fm, name='fm'),
    
    # path('external', views.external, name='external'),
    # path('coba', views.coba, name='coba'),
    # path('signal', views.signal, name='signal')
]