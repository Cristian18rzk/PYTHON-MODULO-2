import pytest
from Ejercicio_11 import validar_cedula


def test_cedula_con_suma_par():
    assert validar_cedula("1234") == True

def test_cedula_con_suma_impar():
    assert validar_cedula("1235") == False

def test_cedula_con_caracteres_no_numericos():
    assert validar_cedula("abcde") == False
    assert validar_cedula("123-4") == False

def test_cedula_vacia():
    assert validar_cedula("") == False

def test_cedula_larga_con_suma_par():
    assert validar_cedula("11111111") == True

def test_cedula_larga_con_suma_impar():
    assert validar_cedula("11111112") == False