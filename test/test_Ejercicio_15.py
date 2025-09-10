import pytest
from Ejercicio_15 import crear_tablero

def test_crear_tablero_tamano_correcto():
    tamano = 5
    tablero = crear_tablero(tamano)
    assert len(tablero) == tamano
    assert all(len(fila) == tamano for fila in tablero)
    assert all(casilla == "O" for fila in tablero for casilla in fila)


def test_crear_tablero_dimensiones():
    tablero = crear_tablero(5)
    assert len(tablero) == 5
    assert all(len(fila) == 5 for fila in tablero)


def test_crear_tablero_contenido_inicial():
    tablero = crear_tablero(3)
    assert all(all(casilla == 'O' for casilla in fila) for fila in tablero)


