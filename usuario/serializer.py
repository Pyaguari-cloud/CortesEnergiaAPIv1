from rest_framework import serializers
from .models import Usuario
from cliente.models import Cliente
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['username', 'rol']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)


        # agregamos campos personalizados

        token['username'] = user.username
        token['role'] = user.rol

        return token
    
class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)

        # Obtener el refresh token
        refresh = RefreshToken(attrs['refresh'])



        # Obtener el usuario asociado al refresh token
        user = Usuario.objects.get(id=refresh['user_id'])

        # Agregar el username y el rol a la respuesta
        data['refresh'] = str(refresh)
        data['username'] = user.username
        data['role'] = user.rol
        data['id'] = user.id
        try:
            cliente = Cliente.objects.get(usuario=user)
            data['cliente_id'] = cliente.id
        except Cliente.DoesNotExist:
            data['cliente_id'] = None
        


        return data