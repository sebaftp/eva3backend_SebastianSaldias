import pandas as pd

# Función para procesar el archivo CSV
def procesar_csv(ruta_archivo):
    # Leer archivo CSV
    df = pd.read_csv(ruta_archivo)
    
    # Limpiar datos: eliminar duplicados y manejar valores nulos
    df = df.drop_duplicates()
    df = df.fillna({
        "Edad": df["Edad"].mean(),  # Reemplazar valores nulos de edad por el promedio
        "Saldo": df["Saldo"].median(),  # Reemplazar valores nulos de saldo por la mediana
        "Genero": "No especificado",  # Genero por defecto
        "Nivel_de_Satisfaccion": 3,  # Nivel neutral si falta información
    })

    # Análisis básico
    promedio_saldo = df["Saldo"].mean()
    distribucion_edades = df["Edad"].value_counts()

    print(f"Promedio de Saldo: {promedio_saldo}")
    print(f"Distribución de Edades: {distribucion_edades}")

    # Exportar datos limpios (opcional, para verificar resultados)
    df.to_csv("clientes_limpios.csv", index=False)

    return df
