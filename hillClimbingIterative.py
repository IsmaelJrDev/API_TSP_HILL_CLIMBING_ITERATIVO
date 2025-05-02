import math
import random

coord = {
    'Jiloyork': (19.916012, -99.580580),
    'Toluca': (19.289165, -99.655697),
    'Atlacomulco': (19.799520, -99.873844),
    'Guadalajara': (20.677754, -103.346253),
    'Monterrey': (25.691611, -100.321838),
    'QuintanaRoo': (21.163112, -86.802315),
    'Michohacan': (19.701400, -101.208297),
    'Aguascalientes': (21.876410, -102.264387),
    'CDMX': (19.432713, -99.133183),
    'QRO': (20.597194, -100.386670)
}

def distancia(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

def evalua_ruta(ruta):
    total = 0
    for i in range(len(ruta) - 1):
        total += distancia(coord[ruta[i]], coord[ruta[i+1]])
    total += distancia(coord[ruta[-1]], coord[ruta[0]])  # regreso al inicio
    return total

def hill_climbing(ciudad_inicio):
    ruta = list(coord.keys())
    ruta.remove(ciudad_inicio)
    random.shuffle(ruta)
    ruta.insert(0, ciudad_inicio)

    mejora = True
    while mejora:
        mejora = False
        dist_actual = evalua_ruta(ruta)
        for i in range(1, len(ruta)):
            for j in range(1, len(ruta)):
                if i != j:
                    ruta_tmp = ruta[:]
                    ruta_tmp[i], ruta_tmp[j] = ruta_tmp[j], ruta_tmp[i]
                    nueva_dist = evalua_ruta(ruta_tmp)
                    if nueva_dist < dist_actual:
                        ruta = ruta_tmp
                        mejora = True
                        break
            if mejora:
                break
    return ruta

def hill_climbing_iterativo(ciudad_inicio, max_iteraciones=10):
    mejor_ruta = None
    mejor_distancia = float('inf')

    for _ in range(max_iteraciones):
        ruta = hill_climbing(ciudad_inicio)
        dist = evalua_ruta(ruta)
        if dist < mejor_distancia:
            mejor_ruta = ruta
            mejor_distancia = dist

    return mejor_ruta, mejor_distancia

def obtener_ciudades():
    return list(coord.keys())
