import pytest
from Ejercicio_9 import pro_iva

def test_calculo_iva_correcto_con_multiples_productos():
    list_productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000}
    ]
    esperado = {"Camisa": 59500.00, "Pantalón": 95200.00}
    assert pro_iva(list_productos) == esperado

def test_calculo_iva_con_un_producto():
    list_productos = [
        {"nombre": "Zapatos", "precio": 100000}
    ]
    esperado = {"Zapatos": 119000.00}
    assert pro_iva(list_productos) == esperado

def test_redondeo_correcto():
    list_productos = [
        {"nombre": "Gorra", "precio": 25000}
    ]
    esperado = {"Gorra": 29750.00}
    assert pro_iva(list_productos) == esperado

def test_lista_vacia_retorna_diccionario_vacio():
    assert pro_iva([]) == {}

def test_diccionario_sin_clave_nombre_lanza_error():
    with pytest.raises(KeyError):
        pro_iva([{"precio": 50000}])