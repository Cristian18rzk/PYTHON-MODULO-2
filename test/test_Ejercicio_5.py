import pytest
from Ejercicio_5 import clasificar_num


def test_par_no_multiplo_de_5():
    assert clasificar_num(4) == "Par"
    assert clasificar_num(2) == "Par"

def test_impar_no_multiplo_de_5():
    assert clasificar_num(3) == "Impar"
    assert clasificar_num(7) == "Impar"

def test_par_y_multiplo_de_5():
    assert clasificar_num(10) == "Par y múltiplo de 5"
    assert clasificar_num(20) == "Par y múltiplo de 5"

def test_impar_y_multiplo_de_5():
    assert clasificar_num(5) == "Impar y múltiplo de 5"
    assert clasificar_num(15) == "Impar y múltiplo de 5"

def test_numero_cero():
    assert clasificar_num(0) == "Par y múltiplo de 5"

def test_numeros_negativos():
    assert clasificar_num(-4) == "Par"
    assert clasificar_num(-5) == "Impar y múltiplo de 5"
    assert clasificar_num(-10) == "Par y múltiplo de 5"

def test_no_acepta_strings():
    with pytest.raises(TypeError):
        clasificar_num("10")

