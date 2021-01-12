from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    email    = serializers.CharField()
    password = serializers.CharField()
    
    def create(self, validate_data):
        instance = User()
        instance.username = validate_data.get('username')
        instance.email = validate_data.get('email')
        instance.set_password(validate_data.get('password'))
        instance.save()
        return instance
    
    def validate_username(self, data):
        users = User.objects.filter(username = data)

        if len(users) != 0:
            raise serializers.ValidationError("Este usuario ya esta registrado")
        else:
            return data
    class Meta:
        model = User
        fields = ('__all__')