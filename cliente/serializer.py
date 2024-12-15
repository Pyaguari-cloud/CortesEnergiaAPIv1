from rest_framework import serializers
from .models import Cliente
from usuario.models import Usuario


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model= Cliente
        fields= '__all__'

    def create(self, validated_data):
        #crear un usuario asociado
        correo = validated_data['correo_electronico']
        username = correo
        password = validated_data['cedula']
        usuario = Usuario.objects.create_user(username=username, password=password, rol='cliente')

        # Crear cliente asociado
        cliente = Cliente.objects.create(usuario=usuario, **validated_data)
        return cliente
    
def update(self, instance, validated_data):
        # Actualizar el usuario asociado si el correo electrónico cambia
        if 'correo_electronico' in validated_data:
            new_email = validated_data['correo_electronico']
            instance.usuario.username = new_email
            instance.usuario.save()

        # Actualizar el cliente
        instance = super().update(instance, validated_data)
        return instance
