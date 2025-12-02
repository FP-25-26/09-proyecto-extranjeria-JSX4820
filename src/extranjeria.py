# - IMPORTS:
from typing import NamedTuple, List
import csv
RegistroExtranjeria = NamedTuple("RegistroExtranjeria", [("distrito",str), ("seccion", str), ("barrio", str), ("pais",str), ("hombres", int), ("mujeres", int)])

# - EJERCICIO 1:
def lee_datos_extranjeria(fichero:str) -> List[RegistroExtranjeria]:
    registros = []
    with open(fichero, encoding = 'utf-8') as f:
        lector = csv.reader(f)
        next(lector)
        for distrito, seccion, barrio, pais, hombres, mujeres in lector:
            distrito = distrito.strip()
            seccion = seccion.strip()
            barrio = barrio.strip()
            pais = pais.strip()
            hombres = int(hombres)
            mujeres = int(mujeres)
            tupla_aux = RegistroExtranjeria(distrito, seccion, barrio, pais, hombres, mujeres)
            registros.append(tupla_aux)
    return registros

# - EJERCICIO 2:
def numero_nacionalidades_distintas(registros:List[RegistroExtranjeria]) -> int:
    nacionalidades = set(registro.pais for registro in registros)
    return len(nacionalidades)

# - EJERCICIO 3:
def secciones_distritos_con_extranjeros_nacionalidades(registros:List[RegistroExtranjeria], paises:set[str]) -> List[tuple]:
    registros_filtrados = [registro for registro in registros if registro.pais in paises]
    secciones_y_distritos = set((registro_f.distrito, registro_f.seccion) for registro_f in registros_filtrados)
    return sorted(secciones_y_distritos)

# - EJERCICIO 4:
def total_extranjeros_por_pais(registros:List[RegistroExtranjeria]) -> dict[str, int]:
    dict_aux = dict()
    for registro in registros:
        if registro.pais in dict_aux:
            dict_aux[registro.pais] += (registro.hombres + registro.mujeres)
        else:
            dict_aux[registro.pais] = (registro.hombres + registro.mujeres)
    return dict_aux

# - EJERCICIO 5:
def top_n_extranjeria(registros:List[RegistroExtranjeria], n:int = 3) -> List[tuple]:
    dict_aux = total_extranjeros_por_pais(registros)
    mas_poblacion = [(clave, valor) for clave, valor in dict_aux.items()]
    mas_poblacion.sort(key=lambda m:m[1], reverse=True)
    return mas_poblacion[:n]

# - EJERCICIO 6:
def barrios_mas_multicultural(registros:List[RegistroExtranjeria]) -> str:
    