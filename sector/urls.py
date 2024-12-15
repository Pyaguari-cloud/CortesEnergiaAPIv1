from django.urls import path
from .views import SectorListView, SectorDetailView

urlpatterns = [
    path('sectores/', SectorListView.as_view(), name='sector-list'),
    path('sectores/<int:pk>/', SectorDetailView.as_view(), name='sector-detail'),
]