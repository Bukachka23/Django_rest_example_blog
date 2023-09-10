"""
    path('admin/', admin.site.urls) - mapping the Django admin interface to the URL path 'admin/'
    path('', include('api.urls')) - including the URLs from the 'api' app at the root URL path
    path('api-auth/', include('rest_framework.urls')) - including the authentication URLs from Django REST Framework
"""

from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')),
    path('api-auth/', include('rest_framework.urls'))
]
