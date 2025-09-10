import pytest
from Ejercicio_3 import Validar_claves

def test_contrasena_valida():
    assert Validar_claves("ClaveValida123") == "Contraseña es Valida."

def test_menos_de_8_caracteres():
    assert Validar_claves("Corta1") == "La Contraseña debe tener al menos 8 caracteres."

def test_sin_mayuscula():
    assert Validar_claves("password123") == "La Contraseña debe contener al menos una mayúscula."

def test_no_acepta_valores_booleanos():
    with pytest.raises(TypeError):
        Validar_claves(True)

def test_no_acepta_numeros_enteros():
    with pytest.raises(TypeError):
        Validar_claves(12345)