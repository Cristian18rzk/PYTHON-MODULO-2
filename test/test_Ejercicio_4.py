import pytest
import random
from Ejercicio_4 import jugar

# --- Nuevas pruebas para entradas numéricas ---

def test_opcion_vacia():
    with pytest.raises(ValueError, match="Opcion no valida use piedra papel o tijeras"):
        jugar("")

def test_opcion_invalida_lanza_error():
    with pytest.raises(ValueError, match="Opcion no valida use piedra papel o tijeras"):
        jugar("lagarto")

def test_opcion_con_mayusculas():
    assert jugar("PIEDRA", "tijeras") == ("piedra", "tijeras", "jugador")

def test_empate():
    assert jugar("piedra", "piedra") == ("piedra", "piedra", "empate")

def test_no_acepta_emojis():
    with pytest.raises(ValueError, match="Opcion no valida use piedra papel o tijeras"):
        jugar("🪨")
