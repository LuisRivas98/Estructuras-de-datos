from Modulo2_hashings.agenda_diccionarios import add_contact, delete_contact, search_contact

def test_add_contact():  #definicion de la función test_add_contact
    contacts = {}  
    add_contact(contacts, "Juan", "123456789")  # Agrega un contacto
    assert contacts == {"Juan": "123456789"}  # Verifica que el contacto se haya agregado

def test_search_contact():  #definicion de la función test_search_contact
    contacts = {"Maria": "987654321"}  
    result = search_contact(contacts, "Maria")  # Busca un contacto existente
    assert result == "Contacto: Maria, Teléfono: 987654321"  # Verifica que la búsqueda sea correcta
    result_not_found = search_contact(contacts, "Luis")  # Busca un contacto inexistente
    assert result_not_found == "Contacto Luis no encontrado"  # Verifica que la búsqueda sea correcta

def test_delete_contact():  #definicion de la función test_delete_contact
    contacts = {"Pedro": "555555555"}  
    result = delete_contact(contacts, "Pedro")  # Elimina un contacto existente
    assert result == "El contacto Pedro ha sido eliminado"  # Verifica que la eliminación sea correcta
    assert contacts == {}  # Verifica que el diccionario de contactos esté vacío
    result_not_found = delete_contact(contacts, "Luis")  # Intenta eliminar un contacto inexistente
    assert result_not_found == "Contacto Luis no encontrado"  # Verifica que la eliminación sea correcta

def test_modify_contact():  #definicion de la función test_modify_contact
    contacts = {"Ana": "111111111"}  
    result = add_contact(contacts, "Ana", "222222222")  # Modifica el contacto existente
    assert contacts == {"Ana": "222222222"}  # Verifica que el contacto se haya modificado correctamente