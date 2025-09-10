import pytest
from Ejercicio_7 import combinar_list, generar_reporte

def test_combinar_listas_correctamente():
    nombres = ["Ana", "Juan", "Maria"]
    notas = [4.5, 3.8, 5.0]
    esperado = {"Ana": 4.5, "Juan": 3.8, "Maria": 5.0}
    assert combinar_list(nombres, notas) == esperado

def test_combinar_con_listas_de_diferente_longitud():
    nombres_mas_largos = ["Pedro", "Luis", "Carlos"]
    notas_mas_cortas = [2.5, 3.0]
    esperado_1 = {"Pedro": 2.5, "Luis": 3.0}
    assert combinar_list(nombres_mas_largos, notas_mas_cortas) == esperado_1

    nombres_mas_cortos = ["Laura", "Sofia"]
    notas_mas_largas = [4.0, 4.2, 3.9]
    esperado_2 = {"Laura": 4.0, "Sofia": 4.2}
    assert combinar_list(nombres_mas_cortos, notas_mas_largas) == esperado_2

def test_combinar_con_listas_vacias():
    assert combinar_list([], []) == {}
    assert combinar_list(["Ana"], []) == {}
    assert combinar_list([], [4.5]) == {}

def test_combinar_con_tipos_incorrectos():
    with pytest.raises(TypeError):
        combinar_list("Ana", 4.5)
    with pytest.raises(TypeError):
        combinar_list(123, [4.5])

def test_generar_reporte_correctamente():
    estudiantes = {"Ana": 4.5, "Juan": 3.8}
    esperado = [
        "El estudiante Ana tiene una nota de 4.5",
        "El estudiante Juan tiene una nota de 3.8"
    ]
    assert generar_reporte(estudiantes) == esperado
