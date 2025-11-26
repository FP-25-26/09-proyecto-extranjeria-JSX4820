from extranjeria import *
def test_lee_datos_extranjeria(fichero:str) -> None:
    print(f"Estos son los registros de extranjería de Sevilla: {lee_datos_extranjeria(fichero)}")
def test_numero_nacionalidades_distintas(registros:List[RegistroExtranjeria]) -> None:
    print(f"Hay un total de {numero_nacionalidades_distintas(registros)} distintas")
def test_secciones_nacionalidades_distintas(registros:List[RegistroExtranjeria], paises:set[str]) -> None:
    print(f"Estos son los distritos y secciones que tienen extranjeros de los países introducidos: {secciones_distritos_con_extranjeros_nacionalidades(registros, paises)}")
if __name__ == "__main__":
    registros = lee_datos_extranjeria("data\extranjeriaSevilla.csv")
    #test_numero_nacionalidades_distintas(registros)
    test_secciones_nacionalidades_distintas(registros, {"ITALIA", "ALEMANIA"})