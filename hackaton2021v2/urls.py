from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('customUser.urls')),
    path('admin/', admin.site.urls),
]
