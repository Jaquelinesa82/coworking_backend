from rest_framework import serializers
from auth_app.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'password', 'first_name', 'last_name']

    def validate_email(self, value):
        """Evita erro ao atualizar o próprio e-mail"""
        user = self.instance
        if CustomUser.objects.filter(email=value).exclude(pk=user.pk if user else None).exists():
            raise serializers.ValidationError("Este e-mail já está em uso.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = CustomUser(**validated_data)
        user.set_password(password)
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance
