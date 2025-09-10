import pytest
import random
from Ejercicio_12 import simular_dados


def test_simular_dados_retorna_diccionario():
    frecuencias = simular_dados(1)
    assert isinstance(frecuencias, dict)


def test_simular_dados_con_cero_lanzamientos():
    frecuencias = simular_dados(0)
    assert frecuencias == {}


def test_simular_dados_rango_de_sumas():
    lanzamientos = 1000
    frecuencias = simular_dados(lanzamientos)

    # Comprobamos que el valor mínimo y máximo en las claves del diccionario
    # estén dentro del rango esperado.
    if frecuencias:
        assert min(frecuencias.keys()) >= 2
        assert max(frecuencias.keys()) <= 12




