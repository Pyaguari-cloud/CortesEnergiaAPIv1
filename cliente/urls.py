from django.urls import path
from .views import ClienteListView, ClienteDetailView

urlpatterns = [
    path('clientes/', ClienteListView.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', ClienteDetailView.as_view(), name='cliente-detail'),
]