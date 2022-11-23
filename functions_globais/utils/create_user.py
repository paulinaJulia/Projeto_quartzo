

def create_user(object, nivel):
    object.nivel = nivel
    object.set_password(object.password)
    object.username = object.cpf
    object.save()
    object.save_permissions()