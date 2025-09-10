import pytest
from Ejercicio_10 import transponer_matriz_de_for, transponer_matriz_de_comprehension

@pytest.mark.parametrize("funcion_transponer", [
    transponer_matriz_de_for,
    transponer_matriz_de_comprehension
])
def test_matriz_transpuesta_correctamente(funcion_transponer):
    matriz_original = [[1, 2, 3], [4, 5, 6]]
    matriz_esperada = [[1, 4], [2, 5], [3, 6]]
    assert funcion_transponer(matriz_original) == matriz_esperada

@pytest.mark.parametrize("funcion_transponer", [
    transponer_matriz_de_for,
    transponer_matriz_de_comprehension
])
def test_matriz_cuadrada(funcion_transponer):
    matriz_original = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz_esperada = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert funcion_transponer(matriz_original) == matriz_esperada

@pytest.mark.parametrize("funcion_transponer", [
    transponer_matriz_de_for,
    transponer_matriz_de_comprehension
])
def test_matriz_de_una_sola_fila(funcion_transponer):
    matriz_original = [[10, 20, 30]]
    matriz_esperada = [[10], [20], [30]]
    assert funcion_transponer(matriz_original) == matriz_esperada


