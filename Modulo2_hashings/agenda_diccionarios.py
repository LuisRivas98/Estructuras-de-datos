contacts = {}

def add_contact(contacts, name, phone):     #funcion para agregar contactos
    if name not in contacts:
        contacts[name] = phone
        return f"Contacto {name} agregado"
    else:
        old_phone = contacts[name]
        contacts[name] = phone
        return f"El contacto {name} se va a modificar, el teléfono anterior era: {old_phone}"
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