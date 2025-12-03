from extranjeria import *
def test_lee_datos_extranjeria(fichero:str) -> None:
    print(f"Estos son los registros de extranjería de Sevilla: {lee_datos_extranjeria(fichero)}")
def test_numero_nacionalidades_distintas(registros:List[RegistroExtranjeria]) -> None:
    print(f"Hay un total de {numero_nacionalidades_distintas(registros)} distintas")
def test_secciones_nacionalidades_distintas(registros:List[RegistroExtranjeria], paises:set[str]) -> None:
    print(f"Estos son los distritos y secciones que tienen extranjeros de los países introducidos: {secciones_distritos_con_extranjeros_nacionalidades(registros, paises)}")
def test_total_extranjeros_por_pais(registros:List[RegistroExtranjeria]) -> None:
    print(f"Estos son el total de extranjeros que hay por cada país: {total_extranjeros_por_pais(registros)}")
def test_top_n_extranjeria(registros:List[RegistroExtranjeria], n:int = 3) -> None:
    print(f"Estos son los {n} países con más población extranjera: {top_n_extranjeria(registros, n)}")
def test_barrio_mas_multicultural(registros:List[RegistroExtranjeria]) -> None:
    print(f"Este es el barrio más multicultural: {barrios_mas_multicultural(registros)}")
def test_barrio_con_mas_extranjeros(registros:List[RegistroExtranjeria], tipo:str = None) -> None:
    print(f"Este es el barrio con más extranjeros: {barrio_con_mas_extranjeros(registros, tipo)}")
if __name__ == "__main__":
    registros = lee_datos_extranjeria("data\extranjeriaSevilla.csv")
    #test_numero_nacionalidades_distintas(registros)
    #test_secciones_nacionalidades_distintas(registros, {"ITALIA", "ALEMANIA"})
    #test_total_extranjeros_por_pais(registros)
    #test_top_n_extranjeria(registros)
    #test_barrio_mas_multicultural(registros)
    test_barrio_con_mas_extranjeros(registros, "Hombres")