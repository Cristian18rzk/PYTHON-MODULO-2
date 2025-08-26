from typing import List, Dict
def combinar_list(nombres: List[str], notas: List[float]) -> Dict[str, float]:
    """
    Combina dos listas en un diccionario {nombre: nota}.

    -----------------------------------------------------------------------------------------------

    Parámetros:
        nombres (List[str]): Lista de nombres de estudiantes.
        notas (List[float]): Lista de notas correspondientes.

    -----------------------------------------------------------------------------------------------

    Retorna:
        Dict[str, float]: Diccionario con nombres como claves y notas como valores.
    """
    return dict(zip(nombres, notas))


def generar_reporte(estudiantes: Dict[str, float]) -> List[str]:
    """
    Genera un reporte a partir de un diccionario de estudiantes y notas.

    -----------------------------------------------------------------------------------------------

    Parámetros:
        estudiantes (Dict[str, float]): Diccionario {nombre: nota}.

    -----------------------------------------------------------------------------------------------

    Retorna:
        List[str]: Lista de frases con el formato "El estudiante [Nombre] tiene una nota de [Nota]".
    """
    return [
        f"El estudiante {nombre} tiene una nota de {nota}"
        for nombre, nota in estudiantes.items()
    ]


if __name__ == "__main__":
    nombres_ingresados: List[str] = input("Ingrese nombres separados por coma: ").split(",")
    notas_ingresadas: List[float] = [float(x) for x in input("Ingrese notas separadas por coma: ").split(",")]

    estudiantes = combinar_list([n.strip() for n in nombres_ingresados], notas_ingresadas)
    for reporte in generar_reporte(estudiantes):
        print(reporte)