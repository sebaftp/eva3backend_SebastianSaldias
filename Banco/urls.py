from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('DatosClientes/', include('DatosClientes.urls')),  # Conectar las URLs de la app
]
