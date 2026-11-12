contacts = {}

def add_contact(contacts, name, phone):     #funcion para agregar contactos
    if name not in contacts:
        contacts[name] = phone
    else:
        contacts[name] = phone  # Actualiza el número de teléfono si el contacto ya existe
        print(f"El contacto {name} ya existe. Se ha actualizado el número de teléfono.")
    return contacts
def search_contact(contacts, name):         #funcion para buscar contactos
    if name in contacts:
        return f"Contacto: {name}, Teléfono: {contacts[name ]}"
    else:
        return f"Contacto {name} no encontrado"
def delete_contact(contacts, name):         #funcion para eliminar contactos
    if name in contacts:
        del contacts[name]
        return f"El contacto {name} ha sido eliminado"
    else:
        return f"Contacto {name} no encontrado"
def show_contacts(contacts):                #funcion para mostrar contacto
    if not contacts:
        print("No hay contactos en la agenda.")
    else:
        print("Contactos en la agenda:")   
    for name, phone in contacts.items():
        print(f"Nombre: {name}, Teléfono: {phone}")

add_contact(contacts, "Juan", "123456789")      #se agrega un contacto
add_contact(contacts, "Maria", "987654321")     #se agrega un contacto
add_contact(contacts, "Pedro", "555555555")     #se agrega un contacto
show_contacts(contacts)                         #muestra contactos
print(f"{search_contact(contacts, "Maria")}")   #busqueda de un contacto existente
print(f"{search_contact(contacts, "Luis")}")    #busqueda de un contacto inexistente
add_contact(contacts, "Maria", "111111111")     #actualiza contacto existente
show_contacts(contacts)                         #muestra contactos
print(f"{delete_contact(contacts, "Juan")}")    #elimina un contacto existente
show_contacts(contacts)                         #muestra contactos
print(f"{delete_contact(contacts, "Luis")}")    #intenta eliminar un contacto inexistente