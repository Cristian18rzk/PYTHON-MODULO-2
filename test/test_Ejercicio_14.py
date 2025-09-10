
import pytest
from Ejercicio_14 import mostrar_ahorcado

def test_mostrar_ahorcado_con_string_lanza_typeerror():
    with pytest.raises(TypeError):
        mostrar_ahorcado("esto_es_un_texto")

def test_mostrar_ahorcado_con_flotante_lanza_typeerror():
    with pytest.raises(TypeError):
        mostrar_ahorcado(3.5)

def test_mostrar_ahorcado_con_lista_lanza_typeerror():
    with pytest.raises(TypeError):
        mostrar_ahorcado([1, 2, 3])

def test_mostrar_ahorcado_con_diccionario_lanza_typeerror():
    with pytest.raises(TypeError):
        mostrar_ahorcado({'intento': 4})

def test_mostrar_ahorcado_con_nulo_lanza_typeerror():
    with pytest.raises(TypeError):
        mostrar_ahorcado(None)