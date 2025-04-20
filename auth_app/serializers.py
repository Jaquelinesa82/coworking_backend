from rest_framework import serializers
from auth_app.models import CustomUser
from django.core.exceptions import ValidationError


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = [
            'id',
            'email',
            'password',
            'first_name',
            'last_name'
        ]
        
    def validate_email(self, value):
        """Verifica se o e-mail já foi cadastrado."""
        if CustomUser.objects.filter(email=value).exists():
            raise ValidationError("Este e-mail já está em uso.")
        return value
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user
