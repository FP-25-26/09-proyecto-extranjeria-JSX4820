from extranjeria import *

# EJERCICIO 1:
def test_lee_datos_extranjeria(fichero:str) -> None:
    print(f"Estos son los registros leídos: {lee_datos_extranjeria(fichero)}")

# EJERCICIO 2:
def test_numero_nacionalidades_distintas(registros:List[RegistroExtranjeria]) -> None:
    print(f"Estas son el total de las distintas distintas nacionalidades encontradas: {numero_nacionalidades_distintas(registros)}")

# EJERCICIO 3:
def test_secciones_distritos_con_extranjeros_nacionalidades(registros:List[RegistroExtranjeria], paises:Set[str]) -> None:
    print(f"Estas son las secciones con extranjeros procedentes de {paises}: {secciones_distritos_con_extranjeros_nacionalidades(registros, paises)[:3]}")

# EJERCICIO 4:
def test_total_extranjeros_por_pais(registros:List[RegistroExtranjeria]) -> None:
    print(f"Estos son los residentes por país que hay: {total_extranjeros_por_pais(registros)}")

# EJERCICIO 5:
def test_top_n_extranjeria(registros:List[RegistroExtranjeria], n:int=3) -> None:
    print(f"Estos son los {n} paises con mayor poblacion: {top_n_extranjeria(registros, n)}")

#EJERCICIO 6:
def test_barrio_mas_multicultural(registros:List[RegistroExtranjeria]) -> None:
    print(f"Este es el barrio más multicultural: {barrio_mas_multicultural(registros)}")

# EJERCICIO 7:
def test_barrio_con_mas_extranjeros(registros:List[RegistroExtranjeria], tipo:str=None) -> str:
    print(f"Este es el barrio con más extranjeros {tipo.lower()} {barrio_con_mas_extranjeros(registros, tipo)}")

# EJERCICIO 8 :
def test_pais_mas_representado_por_distrito(registros:List[RegistroExtranjeria]) -> None:
    print(f"Este es el país más representado por distrito: {pais_mas_representado_por_distrito(registros)}")

if __name__ == "__main__":
    registros = lee_datos_extranjeria("data/extranjeriaSevilla.csv")
    #test_lee_datos_extranjeria("data/extranjeriaSevilla.csv")
    #test_numero_nacionalidades_distintas(registros)
    #test_secciones_distritos_con_extranjeros_nacionalidades(registros, {"ITALIA", "ALEMANIA"})
    #test_total_extranjeros_por_pais(registros)
    #test_top_n_extranjeria(registros, 5)
    #test_barrio_mas_multicultural(registros)
    #test_barrio_con_mas_extranjeros(registros, "Mujeres")
    test_pais_mas_representado_por_distrito(registros)