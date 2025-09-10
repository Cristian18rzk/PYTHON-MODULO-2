import pytest
from Ejercicio_13 import aventura_templo

def test_victoria_camino_rapido():
    acciones = ["este", "examinar"]
    resultado = aventura_templo(acciones)
    assert resultado == "victoria"

def test_derrota_por_trampa():
    acciones = ["norte", "continuar"]
    resultado = aventura_templo(acciones)
    assert resultado == "derrota_trampa"

def test_derrota_por_falta_de_movimientos():
    acciones = ["este", "volver", "norte", "correr"]
    resultado = aventura_templo(acciones)
    assert resultado == "derrota_tiempo"

def test_victoria_con_movimientos_extra():
    acciones = ["este", "examinar", "norte", "continuar"]  # Acciones de más
    resultado = aventura_templo(acciones)
    assert resultado == "victoria"




