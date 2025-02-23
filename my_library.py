def valor_num(diccionario):
    lista_valores = []
    if isinstance(diccionario, dict):
        for clave, valor in diccionario.items():
            if isinstance(valor, dict):
                lista_valores.extend(valor_num(valor))
            elif isinstance(valor, (int, float)):
                lista_valores.append(valor)
    return lista_valores

def calcular_10_de_la_suma(suma):
    return suma * 0.10

def calcular_5_de_la_suma (suma):
    return suma * 0.05

def name_platos(diccionario):
    lista_platos = []
    if isinstance(diccionario, dict):
        for clave, valor in diccionario.items():
            if isinstance(valor, dict):
                lista_platos.append(clave)
    return lista_platos

def calcular_nutrientes (clave,claves):
    nutriente = (clave/100)*claves
    return nutriente

def coger_el_numero(diccionario):
    platos_gramos_tipos = set()
    if isinstance(diccionario, dict):
        for clave, valor in diccionario.items():
            if isinstance(valor, dict):
                for clave_plato, valor_plato in valor.items():
                    if 'number_um' in valor is not None and 'type' in valor is not None:
                        platos_gramos_tipos.add((clave, valor['number_um'],valor['type']))
    return list(platos_gramos_tipos)

def promedio (diccionario,clave):
    return round(sum(diccionario[clave])/len(diccionario[clave]))







                             

