from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cliente
from .serializer import ClienteSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

class ClienteListView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Obtener todos los clientes", responses={200: ClienteSerializer(many=True)})
    def get(self, request):
        clientes = Cliente.objects.all()
        serializer = ClienteSerializer(clientes, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Crear un cliente", request_body=ClienteSerializer, responses={201: openapi.Response("Cliente creado exitosamente")})
    def post(self, request):
        cedula = request.data.get('cedula')
        correo_electronico = request.data.get('correo_electronico')

        if Cliente.objects.filter(cedula=cedula).exists():
            return Response({"error": "La cédula ya existe"}, status=status.HTTP_400_BAD_REQUEST)
        
        if Cliente.objects.filter(correo_electronico=correo_electronico).exists():
            return Response({"error": "El correo electrónico ya existe"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = ClienteSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({"message": 'Cliente creado exitosamente'}, status=status.HTTP_201_CREATED)
        return Response({"error": 'Datos no válidos'}, status=status.HTTP_400_BAD_REQUEST)
    
class ClienteDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Cliente.objects.get(pk=pk)
        except Cliente.DoesNotExist:
            return None
        
    @swagger_auto_schema(operation_description="Obtener un cliente", responses={200: ClienteSerializer()})
    def get(self, request, pk):
        cliente = self.get_object(pk)
        if cliente is None:
            return Response({"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClienteSerializer(cliente)
        print(request.user.id)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Actualizar un cliente", request_body=ClienteSerializer, responses={200: openapi.Response("Cliente actualizado exitosamente")})
    def put(self, request, pk):
        cliente = self.get_object(pk)
        if cliente is None:
            return Response({"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ClienteSerializer(cliente, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Cliente actualizado exitosamente"}, status=status.HTTP_200_OK)
        return Response({"error": "Datos no válidos"}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(operation_description="Eliminar un cliente", responses={204: openapi.Response("Cliente eliminado exitosamente")})
    def delete(self, request, pk):
        cliente = self.get_object(pk)
        if cliente is None:
            return Response({"error": "Cliente no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        cliente.delete()
        return Response({"message": "Cliente eliminado exitosamente"}, status=status.HTTP_204_NO_CONTENT)