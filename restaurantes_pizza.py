import json
import os

# Función para leer los datos desde un archivo JSON
def leer_datos_json(file_name):
    with open(file_name, 'r') as file:
        return json.load(file)

# Lista de archivos JSON
file_names = ['Atlanta.json', 'Don Burguer.json', 'El Farallon.json', 'El Triangulo', 'La Paila','Razones y Motivos.json']

# Diccionario para almacenar los restaurantes que venden pizzas por localidad
pizzas_por_localidad = {}

# Leer los menús desde cada archivo JSON y separar los restaurantes por localidad
for file_name in file_names:
    datos = leer_datos_json(file_name)
    localidad = datos['location']
    menu = datos['menu'].get('pizzas', {})

    if menu:
        if localidad not in pizzas_por_localidad:
            pizzas_por_localidad[localidad] = []
        pizzas_por_localidad[localidad].append(datos['nombre'])

# Mostrar los resultados
for localidad, restaurantes in pizzas_por_localidad.items():
    print(f"Localidad: {localidad}")
    for restaurante in restaurantes:
        print(f"  - {restaurante}")
