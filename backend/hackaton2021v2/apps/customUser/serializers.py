from rest_framework import serializers
from .models import improvedUserModel


class UserSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='name.username')
    class Meta:
        model = improvedUserModel
        fields = ['id', 'user', 'role']