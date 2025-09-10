import pytest
from Ejercicio_8 import procesar_list


def test_lista_con_positivos_y_negativos():
    numeros = [-5, 10, -15, 20]
    positivos_esperados = [10, 20]
    negativos_esperados = [-5, -15]
    cuadrados_esperados = [25, 100, 225, 400]
    etiquetas_esperadas = ["negativo", "positivo", "negativo", "positivo"]

    positivos, negativos, cuadrados, etiquetas = procesar_list(numeros)

    assert positivos == positivos_esperados
    assert negativos == negativos_esperados
    assert cuadrados == cuadrados_esperados
    assert etiquetas == etiquetas_esperadas


def test_lista_solo_positivos():

    numeros = [1, 2, 3, 4]
    positivos_esperados = [1, 2, 3, 4]
    negativos_esperados = []
    cuadrados_esperados = [1, 4, 9, 16]
    etiquetas_esperadas = ["positivo", "positivo", "positivo", "positivo"]

    positivos, negativos, cuadrados, etiquetas = procesar_list(numeros)

    assert positivos == positivos_esperados
    assert negativos == negativos_esperados
    assert cuadrados == cuadrados_esperados
    assert etiquetas == etiquetas_esperadas

def test_lista_vacia():
    positivos, negativos, cuadrados, etiquetas = procesar_list([])

    assert positivos == []
    assert negativos == []
    assert cuadrados == []
    assert etiquetas == []

def test_entrada_no_lista():
    with pytest.raises(TypeError):
        procesar_list("esto es una cadena")
    with pytest.raises(TypeError):
        procesar_list(12345)
    with pytest.raises(TypeError):
        procesar_list(None)

def test_lista_con_elementos_no_numericos():
    with pytest.raises(TypeError):
        procesar_list([1, "dos", 3])