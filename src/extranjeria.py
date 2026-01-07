from typing import NamedTuple, List, Tuple, Set, Dict
from collections import defaultdict
import csv
RegistroExtranjeria = NamedTuple("RegistroExtranjeria", [("distrito",str), ("seccion", str), ("barrio", str), ("pais",str), ("hombres", int), ("mujeres", int)])

# EJERCICIO 1:
def lee_datos_extranjeria(fichero:str) -> List[RegistroExtranjeria]:
    registros = []
    with open(fichero, encoding='utf-8') as f:
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

# EJERCICIO 2:
def numero_nacionalidades_distintas(registros:List[RegistroExtranjeria]) -> int:
    nacionalidades = set(registro.pais for registro in registros)
    return len(nacionalidades)

# EJERCICIO 3:
def secciones_distritos_con_extranjeros_nacionalidades(registros:List[RegistroExtranjeria], paises:Set[str]) -> Tuple[str, str]:
    secciones_extranjeros = set((r.distrito, r.seccion) for r in registros if r.pais in paises)
    return sorted(secciones_extranjeros)

# EJERCICIO 4:
def total_extranjeros_por_pais(registros:List[RegistroExtranjeria]) -> Dict[str, int]:
    extranjeros = defaultdict(int)
    for r in registros:
        extranjeros[r.pais] += (r.hombres + r.mujeres)
    return extranjeros

# EJERCICIO 5:
def top_n_extranjeria(registros:List[RegistroExtranjeria], n:int=3) -> Tuple[str, int]:
    dict_aux = total_extranjeros_por_pais(registros)
    list_aux = sorted(dict_aux.items(), key=lambda i:i[1], reverse=True)
    mayor_poblacion = [(i[0], i[1]) for i in list_aux[:n]]
    return mayor_poblacion

# EJERCICIO 6:
def paises_por_barrio(registros:List[RegistroExtranjeria]) -> Dict[str, Set[str]]:
    dict_aux = defaultdict(set)
    for r in registros:
        dict_aux[r.barrio].add(r.pais)
    return dict_aux

def barrio_mas_multicultural(registros:List[RegistroExtranjeria]) -> str:
    dict_aux = paises_por_barrio(registros)
    list_aux = list(dict_aux.items())
    return max(list_aux, key=lambda i:len(i[1]))[0]

# EJERCICIO 7:
def total_extranjeros_por_barrio(registros:List[RegistroExtranjeria], tipo:str=None) -> Dict[str, int]:
    extranjeros = defaultdict(int)
    for r in registros:
        if tipo == "Hombres":
            extranjeros[r.barrio] += r.hombres
        elif tipo == "Mujeres":
            extranjeros[r.barrio] += r.mujeres
        else:
            extranjeros[r.barrio] += (r.hombres + r.mujeres)
    return extranjeros

def barrio_con_mas_extranjeros(registros:List[RegistroExtranjeria], tipo:str=None) -> str:
    dict_aux = total_extranjeros_por_barrio(registros, tipo)
    list_aux = list(dict_aux.items())
    return max(list_aux, key=lambda i:i[1])[0]

# EJERCICIO 8:
def extranjeros_por_distrito(registros:List[RegistroExtranjeria]) -> Dict[str, List[Tuple[str, int]]]:
    dict_aux = defaultdict(lambda: defaultdict(int))
    for r in registros:
        dict_aux[r.distrito][r.pais] += (r.hombres + r.mujeres)
    return dict_aux

def pais_mas_representado_por_distrito(registros:List[RegistroExtranjeria]) -> Dict[str, str]:
    dict_aux = extranjeros_por_distrito(registros)
    pais_representado = dict()
    for clave, valor in dict_aux.items():
        pais_representado[clave] = max(valor.items(), key=lambda i:i[1])[0]
    return pais_representado