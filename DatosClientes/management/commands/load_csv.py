import csv
from django.core.management.base import BaseCommand
from DatosClientes.models import Cliente


class Command(BaseCommand):
    help = 'Carga datos del CSV al modelo Cliente, manejando datos faltantes'

    def clean_float(self, value, default=0.0):
        try:
            return float(value)
        except (ValueError, TypeError):
            return default  # Devuelve un valor predeterminado si es inválido

    def clean_int(self, value, default=0):
        try:
            return int(float(value))  # Maneja valores como "1.0"
        except (ValueError, TypeError):
            return default

    def clean_bool(self, value, default=False):
        try:
            return bool(int(float(value)))
        except (ValueError, TypeError):
            return default

    def clean_str(self, value, default="Desconocido"):
        if value and value.strip():
            return value.strip()
        return default

    def handle(self, *args, **kwargs):
        with open('clientes_banco.csv', 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                cliente_id = self.clean_str(row.get('Cliente_ID'), default=f"ID_Desconocido_{row.get('Edad', '')}")
                edad = self.clean_int(row.get('Edad'), default=0)
                genero = self.clean_str(row.get('Genero'), default="No especificado")
                saldo = self.clean_float(row.get('Saldo'), default=0.0)
                activo = self.clean_bool(row.get('Activo'), default=False)
                nivel_de_satisfaccion = self.clean_int(row.get('Nivel_de_Satisfaccion'), default=1)

                # Intenta crear o actualizar el cliente
                try:
                    cliente, created = Cliente.objects.update_or_create(
                        cliente_id=cliente_id,
                        defaults={
                            'edad': edad,
                            'genero': genero,
                            'saldo': saldo,
                            'activo': activo,
                            'nivel_de_satisfaccion': nivel_de_satisfaccion,
                        }
                    )
                    if created:
                        self.stdout.write(self.style.SUCCESS(f"Cliente creado: {cliente_id}"))
                    else:
                        self.stdout.write(self.style.WARNING(f"Cliente actualizado: {cliente_id}"))
                except Exception as e:
                    self.stderr.write(self.style.ERROR(f"Error al procesar la fila {row}: {e}"))

        self.stdout.write(self.style.SUCCESS('Datos cargados exitosamente'))
