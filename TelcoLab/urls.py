from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('TelcoWeb.urls')),
    path('older/', include('TelcoWebOlder.urls')),
    path('oldest/', include('TelcoWebOldest.urls')),
]
