import pytest
from Ejercicio_2 import consola

def test_comando_guardar_retorna_mensaje_correcto():
    assert consola("guardar") == "Guardando archivo..."

def test_comando_cargar_retorna_mensaje_correcto():
    assert consola("cargar") == "Cargando archivo..."

def test_comando_salir_retorna_mensaje_correcto():
    assert consola("salir") == "Saliendo del programa..."

def test_comando_no_reconocido_retorna_mensaje_correcto():
    assert consola("comando_invalido") == "El Comando no se reconoce."

def test_no_acepta_numeros():
    assert consola("12345") == "El Comando no se reconoce."
    assert consola("1") == "El Comando no se reconoce."
    assert consola("0") == "El Comando no se reconoce."