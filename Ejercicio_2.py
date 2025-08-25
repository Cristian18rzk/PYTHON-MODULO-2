def consola(comando: str) -> str:
    """
    Simula la ejecución de un comando de consola.

    -----------------------------------------------------

    Comandos válidos:
    - "guardar": retorna "Guardando archivo..."
    - "cargar": retorna "Cargando archivo..."
    - "salir": retorna "Saliendo del programa..."

    -----------------------------------------------------

    Parámetros:
        comando (str): texto del comando.

    -----------------------------------------------------

    Retorna:
        str: mensaje de resultado de la acción.
    """
    match comando.lower():
        case "guardar":
            return "Guardando archivo..."
        case "cargar":
            return "Cargando archivo..."
        case "salir":
            return "Saliendo del programa..."
        case _:
            return "El Comando no se reconoce."


if __name__ == "__main__":
    while True:
        mensaje = input("Ingrese un comando (Guardar/Cargar/Salir): ").strip().lower().replace(" ","")
        resultado = consola(mensaje)
        print(resultado)
        if mensaje == "salir":
            break
