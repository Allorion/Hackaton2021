from django.urls import path
from . import views

urlpatterns = [
    path('request-help', views.GetRequestForHelp.as_view(), name='getHelp'),
    path('find-request-help', views.PostRequestForHelp.as_view(), name='postHelp'),
]