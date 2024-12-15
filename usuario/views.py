from cliente.models import Cliente
from .serializer import UsuarioSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .serializer import CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer
from django.contrib.auth import authenticate


# Create your views here.

class UsuarioView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(operation_description="Obtener un usuario", responses={200: UsuarioSerializer()})
    
    def get(self, request):
        serializer = UsuarioSerializer(request.user)
        print(request.user)
        return Response(serializer.data)
    

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            try:

                cliente = Cliente.objects.get(usuario=user)
                response.data['message'] = 'Inicio de sesión exitoso'
                response.data['username'] = user.username
                response.data['role'] = user.rol
                response.data['id'] = user.id
                response.data['cliente_id'] = cliente.id
            except Cliente.DoesNotExist:
                response.data['message'] = 'No se encontró el cliente asociado al usuario'
                response.data['username'] = user.username
                response.data['role'] = user.rol
                response.data['id'] = user.id
        else:
            response.data['message'] = 'Credenciales inválidas'
        print(response.data)
        return response
 
class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        print(response.data)
        return response

        

