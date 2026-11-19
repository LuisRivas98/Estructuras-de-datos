from Modulo2_hashings import consultas_sistema

def test_add_user():
    # Agregar un nuevo usuario
    result = consultas_sistema.add_user("juan", "juan@ejemplo.com")
    assert result == "Usuario juan agregado"
def test_search_email():
    # Buscar un usuario existente
    result = consultas_sistema.search_email("ana_perez")
    assert result == "ana@ejemplo.com"
    # Buscar un usuario inexistente
    result_not_found = consultas_sistema.search_email("luis_rivas")
    assert result_not_found == "Usuario no encontrado"
def test_clean_records():
    contacts = ["ana_perez", "carlos_g", "luis_rivas", "ana_perez", "carlos_g"]
    # Limpiar registros duplicados
    unicos = consultas_sistema.clean_records(contacts)
    assert unicos == {"ana_perez", "carlos_g", "luis_rivas"}
    assert len(unicos) < len(contacts)