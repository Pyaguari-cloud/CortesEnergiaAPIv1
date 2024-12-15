from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Sector
from .serializer import SectorSerializer
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


class SectorListView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Obtener todos los sectores", responses={200: SectorSerializer(many=True)})
    def get(self, request):
        sectores = Sector.objects.all()
        serializer = SectorSerializer(sectores, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(operation_description="Crear un sector", request_body=SectorSerializer, responses={201: openapi.Response("Sector creado exitosamente")})
    def post(self, request):
        sector = request.data.get('nombre')

        if Sector.objects.filter(nombre=sector).exists():
            return Response({"error": "El sector ya existe"}, status=status.HTTP_400_BAD_REQUEST)
        
        serializer = SectorSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Sector creado exitosamente"}, status=status.HTTP_201_CREATED)
        return Response({"error": 'Datos no válidos'}, status=status.HTTP_400_BAD_REQUEST)

class SectorDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Sector.objects.get(pk=pk)
        except Sector.DoesNotExist:
            return None
        
    @swagger_auto_schema(operation_description="Obtener un sector", responses={200: SectorSerializer()})
    def get(self, request, pk):
        sector = self.get_object(pk)
        if sector is None:
            return Response({"error": "Sector no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SectorSerializer(sector)
        return Response(serializer.data)
    

    @swagger_auto_schema(operation_description="Actualizar un sector", request_body=SectorSerializer, responses={200: openapi.Response("Sector actualizado exitosamente")})
    def put(self, request, pk):
        sector = self.get_object(pk)
        if sector is None:
            return Response({"error": "Sector no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SectorSerializer(sector, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Sector actualizado exitosamente"})
        return Response({"error": "Datos no válidos"}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(operation_description="Eliminar un sector", responses={204: openapi.Response("Sector eliminado exitosamente")})
    def delete(self, request, pk):
        sector = self.get_object(pk)
        if sector is None:
            return Response({"error": "Sector no encontrado"}, status=status.HTTP_404_NOT_FOUND)
        sector.delete()
        return Response({"message": "Sector eliminado exitosamente"}, status=status.HTTP_204_NO_CONTENT)