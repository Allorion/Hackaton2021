from django.views.generic import DetailView
from .models import improvedUserModel
from rest_framework import generics
from . import serializers


class UserList(generics.ListAPIView):
    queryset = improvedUserModel.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = improvedUserModel.objects.all()
    serializer_class = serializers.UserSerializer

class UserProfileView(DetailView):
    """ Вывод профиля пользователя """
    model = improvedUserModel
    template_name = 'user/profile.html'
    context_object_name = 'profile'