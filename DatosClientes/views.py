from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from rest_framework import viewsets
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django_filters.rest_framework import DjangoFilterBackend
from .models import Cliente
from .serializers import ClienteSerializer
from django.shortcuts import render
from django_filters.views import FilterView


class ClienteFilter(filters.FilterSet):
    genero = filters.ChoiceFilter(choices=Cliente.GENERO_CHOICES, label="Género")
    activo = filters.BooleanFilter(field_name='activo', label="Activo")
    nivel_de_satisfaccion = filters.ChoiceFilter(choices=Cliente.NIVEL_SATISFACCION_CHOICES, label="Nivel de Satisfacción")

    class Meta:
        model = Cliente
        fields = ['genero', 'activo', 'nivel_de_satisfaccion']

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend]  # Opcional si está en settings.py
    filterset_class = ClienteFilter

def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'Cliente/list.html', {'clientes': clientes})
#CLIENTE LISTA
class ClienteListView(ListView):
    model = Cliente
    template_name = 'cliente/list.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset = super().get_queryset()
        genero = self.request.GET.get('genero')
        nivel_de_satisfaccion = self.request.GET.get('nivel_de_satisfaccion')
        activo = self.request.GET.get('activo')  # Captura el parámetro activo

        if genero:
            queryset = queryset.filter(genero=genero)
        if nivel_de_satisfaccion:
            queryset = queryset.filter(nivel_de_satisfaccion=nivel_de_satisfaccion)
        if activo in ['0', '1']:  # Verifica si "activo" tiene valores válidos
            queryset = queryset.filter(activo=bool(int(activo)))

        return queryset

class ClienteCreateView(CreateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente/create.html'
    success_url = reverse_lazy('cliente-list')
#ACTUALIZAR CLIENTE
class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = '__all__'
    template_name = 'cliente/update.html'
    success_url = reverse_lazy('cliente-list')
#BORRAR CLIENTE
class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = 'cliente/delete.html'
    success_url = reverse_lazy('cliente-list')