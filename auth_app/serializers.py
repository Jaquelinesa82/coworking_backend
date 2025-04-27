from rest_framework import serializers
from auth_app.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

    def validate_email(self, email):
        """Evita erro ao atualizar o próprio e-mail"""
        user = self.instance
        if CustomUser.objects.filter(email=email).exclude(pk=user.pk if user else None).exists():
            raise serializers.ValidationError("Este e-mail já está em uso.")
        return email

    def validate(self, data):
        missing_fields = []
        required_fields = ['email', 'password', 'first_name', 'last_name']

        for field in required_fields:
            # Tratar campos que podem vir vazios por engano
            if not data.get(field) or not str(data.get(field)).strip():
                missing_fields.append(field)

        if missing_fields:
            raise serializers.ValidationError({field: f"O campo '{field}' é obrigatório." for field in missing_fields})

        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
        )
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Adicione campos extras no token se quiser
        token['email'] = user.email
        token['first_name'] = user.first_name
        return token

    def validate(self, attrs):
        # Suporte para email em vez de username
        attrs['username'] = attrs.get('email')
        return super().validate(attrs)
