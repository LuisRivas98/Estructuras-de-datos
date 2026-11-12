top_peliculas = ["The Shawshank Redemption", "The Exorcist", "Goodfellas"] #Lista
coordenadas_CDMX = (19.4326, 99.1332) #Tupla
lenguajes_programacion = {"Python", "JavaScript", "C++", "Python"}  # Python se repite, pero solo aparecerá una vez
libro = {
    "Titulo": "Misery",
    "Autor": "Stephen King",
    "Año": 1987,
}

print(type(top_peliculas))  # Salida: <class 'list'>
print(type(coordenadas_CDMX))  # Salida: <class 'tuple'>
print(type(lenguajes_programacion))  # Salida: <class 'set'>
print(type(libro))  # Salida: <class 'dict'>

print(top_peliculas[0])  # Acceso por índice: Salida: The Shawshank Redemption

#coordenadas_CDMX[0] = 20.0  # TypeError: 'tuple' object does not support item assignment

print(list(lenguajes_programacion))  # Convertir set a lista para mostrar elementos: Salida: ['Python', 'C++', 'JavaScript']
