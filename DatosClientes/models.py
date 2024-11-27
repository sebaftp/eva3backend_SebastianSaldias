from django.db import models

class Cliente(models.Model):
    cliente_id = models.CharField(max_length=50, unique=True)
    
    # Definimos las opciones de género
    GENERO_CHOICES = [
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
    ]
    
    # Definimos las opciones de satisfacción
    NIVEL_SATISFACCION_CHOICES = [
        (1, 'Muy Insatisfecho'),
        (2, 'Insatisfecho'),
        (3, 'Neutral'),
        (4, 'Satisfecho'),
        (5, 'Muy Satisfecho'),
    ]

    edad = models.PositiveSmallIntegerField(help_text="Edad del cliente.")
    genero = models.CharField(
        max_length=10, 
        choices=GENERO_CHOICES, 
        help_text="Género del cliente (Masculino, Femenino)."
    )
    saldo = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        help_text="Saldo promedio en la cuenta."
    )
    activo = models.BooleanField(
        default=True, 
        help_text="Estado de actividad del cliente (1: Activo, 0: Inactivo)."
    )
    nivel_de_satisfaccion = models.IntegerField(choices=NIVEL_SATISFACCION_CHOICES)
    
    def __str__(self):
        return f"Cliente {self.cliente_id} - {self.genero}, Edad: {self.edad}"
