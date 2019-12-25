from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('compiler/', include('compiler.urls', namespace="compiler")),
    path('', include('user.urls')),
    path('accounts/', include('allauth.urls')),
]
