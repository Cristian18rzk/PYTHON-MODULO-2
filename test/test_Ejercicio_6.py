import pytest
from Ejercicio_6 import encontrar_indices


def test_frase_vacia():
    assert encontrar_indices("", "a") == []

def test_parametro_frase_no_string():
    with pytest.raises(TypeError):
        encontrar_indices(123, "a")
    with pytest.raises(TypeError):
        encontrar_indices(None, "a")

def test_parametro_letra_no_string():
    with pytest.raises(TypeError):
        encontrar_indices("Hola", 1)
    with pytest.raises(TypeError):
        encontrar_indices("Hola", True)

def test_encontrar_multiples_instancias():
    assert encontrar_indices("banana", "a") == [1, 3, 5]

def test_encontrar_una_instancia():
    assert encontrar_indices("Hola mundo", "H") == [0]