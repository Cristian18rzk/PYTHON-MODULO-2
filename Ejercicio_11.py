from typing import Tuple
def validar_cedula(cedula: str) -> bool:
    """
    Valida una cédula verificando si la suma de sus dígitos es par.

    ------------------------------------------------------------------

    Parámetros:
        cedula (str): Número de cédula en formato string.

    ------------------------------------------------------------------

    Retorna:
        bool: True si la cédula es válida, False en caso contrario.
    """
    if not cedula.isdigit():
        return False

    suma = sum(int(digito) for digito in cedula)
    return suma % 2 == 0


def pedir_la_cedula() -> Tuple[str, bool]:
    """
    Pide al usuario una cédula hasta que ingrese una válida.
    Retorna la cédula y el resultado de la validación.
    """
    while True:
        cedula = input("Ingresa Tu cédula: ")
        if validar_cedula(cedula):
            print(f"{True}Cédula válida:", cedula)
            return cedula, True
        else:
            print(f"{False}Cédula no válida inténtalo nuevamente Porfavor.")


if __name__ == "__main__":
    pedir_la_cedula()