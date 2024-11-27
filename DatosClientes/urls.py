from django.urls import path
from .views import ClienteListView, ClienteCreateView, ClienteUpdateView, ClienteDeleteView

urlpatterns = [
    path('cliente/', ClienteListView.as_view(), name='cliente-list'),
    path('cliente/create/', ClienteCreateView.as_view(), name='cliente-create'),
    path('cliente/update/<int:pk>/', ClienteUpdateView.as_view(), name='cliente-update'),
    path('cliente/delete/<int:pk>/', ClienteDeleteView.as_view(), name='cliente-delete'),
]
