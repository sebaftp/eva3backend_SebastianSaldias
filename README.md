1. Localizar la carpeta eva3backend en el escritorio

2. Abrir cmd y poner la ubicación de la carpeta, Ejemplo: cd C:\Users\Sebas\OneDrive\Escritorio\eva3backend

3. Activar el ambiente virtual con .\env\Scripts\actívate

4. Instalar django, Jupyter y djangorestframework, en la cmd ejecutar los siguiete comando

    pip install Django

    pip install djangorestframework

    pip install jupyter pandas

5. Asegurar que el CSV con los datos del cliente se encuentren ubicados en eva3backend tal que la ruta sea así, Ejemplo: C:\Users\Sebas\OneDrive\Escritorio\eva3backend\clientes_banco.csv

6. Correr Jupyter,escribir en la cmd el siguiente código (usando el ambiente virtual): jupyter notebook  (En el caso que no funcione, probar con "jupyter-notebook")

7. Dentro del notebook de jupyter vamos a seleccionar LimpiarCSV, apretamos en "Run" y nos crea el archivo de clientes_banco_limpio.csv con los datos limpios

8. Correr django, escribir en la cmd el siguiente código (usando el ambiente virtual): py manage.py runserver (En el caso que no funcione "py" probar con un "python" o "python3") 

