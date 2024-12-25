import json
import matplotlib.pyplot as plt

# Lista de archivos JSON
file_names = ['Atlanta.json', 'Don_Burguer.json', 'El_Farallon.json', 'El_Triangulo.json', 'La_Paila.json', 'Razones_y_Motivos.json']

# Función para leer los datos desde un archivo JSON
def leer_datos_json(file_name):
    with open(file_name, 'r', encoding="utf8") as file:
        return json.load(file)

# Diccionario para almacenar los restaurantes que venden pizzas por municipio
pizzas_por_municipio = {}

# Leer los menús desde cada archivo JSON y separar los restaurantes por municipio
for file_name in file_names:
    datos = leer_datos_json(file_name)
    municipio = datos['localidad'].get('municipio', {})
    menu = datos['menu'].get('pizzas', {})

    if menu:
        if municipio not in pizzas_por_municipio:
            pizzas_por_municipio[municipio] = 0
        pizzas_por_municipio[municipio] += 1

# Mostrar los resultados
for municipio, cantidad in pizzas_por_municipio.items():
    print(f"Municipio: {municipio}, Restaurantes: {cantidad}")

# Paso 2: Crear la gráfica de barras
municipios = list(pizzas_por_municipio.keys())
cantidad_restaurantes = list(pizzas_por_municipio.values())

plt.bar(municipios, cantidad_restaurantes, color='blue')

# Personalizar la gráfica
plt.xlabel('Municipios')
plt.ylabel('Cantidad de Restaurantes')
plt.title('Cantidad de Restaurantes que Venden Pizzas por Municipio')

# Mostrar la gráfica
plt.xticks(rotation=45)
plt.show()


