import pytest
from Ejercicio_1 import entradas

def test_edad_no_acepta_strings():
    with pytest.raises(TypeError):
        entradas(edad="10")

def test_estudiante_no_acepta_numero():
    with pytest.raises(TypeError):
        entradas(es_estudiante=10)

def test_no_vacios():
    with pytest.raises(TypeError):
        entradas()

def test_edad_no_decimales():
    with pytest.raises(TypeError):
        entradas(edad=10.5)

def test_nino_sin_descuento():
    assert entradas(5, "no") == 10000

def test_estudiante_nino_con_descuento():
    assert entradas(10, "si") == 9000


