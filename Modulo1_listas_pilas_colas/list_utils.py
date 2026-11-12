def buscar_y_filtrar(lista_elementos, criterio):
    return [elemento for elemento in lista_elementos if criterio(elemento)]

print (buscar_y_filtrar([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], lambda x: x > 3))  # Salida: [4, 5, 6, 7, 8, 9, 10]