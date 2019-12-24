from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('compiler/', include('compiler.urls')),
    path('', include('user.urls')),
]
