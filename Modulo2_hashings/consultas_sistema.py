users = {
    "ana_perez": "ana@ejemplo.com",
    "carlos_g": "carlos@ejemplo.com"
}

def add_user(name, email):
    if name not in users:
        users[name] = email
        return f"Usuario {name} agregado"
    else:
        email_antiguo = users[name]
        users[name] = email
        return f"El usuario {name} se va a modificar, el correo anterior era: {email_antiguo}"
def search_email(user):
    return users.get(user, "Usuario no encontrado")
def clean_records(list_ids):
    return set(list_ids)  # Devuelve un conjunto con los IDs únicos, eliminando duplicados