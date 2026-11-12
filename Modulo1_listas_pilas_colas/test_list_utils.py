
from list_utils import buscar_y_filtrar


def test_busqueda_exitosa():
    lista = [1, 2, 3, 4, 5]
    criterio = lambda x: x > 3
    resultado = buscar_y_filtrar(lista, criterio)
    assert resultado == [4, 5]

def test_lista_vacia():
    lista = []
    criterio = lambda x: x > 3
    resultado = buscar_y_filtrar(lista, criterio)
    assert resultado == []

def test_sin_coincidencias():
    lista = [1, 2, 3]
    criterio = lambda x: x > 3
    resultado = buscar_y_filtrar(lista, criterio)
    assert resultado == []