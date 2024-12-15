from django.urls import path
from .views import UsuarioView,CustomTokenObtainPairView, CustomTokenRefreshView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('usuario/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('usuario/', UsuarioView.as_view(), name='usuario'),
    path('usuario/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]
