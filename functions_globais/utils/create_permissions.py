
def create_permision(codename, name, ct):
    from django.contrib.auth.models import Permission 

    try:
        return Permission.objects.get(codename =codename) 
    except Exception:
        return Permission.objects.create(codename =codename, 
                                                    name=name, 
                                                            content_type = ct) 
#codigos que criam a permição 
def create_permissions(model, call_back):
    from django.contrib.auth.models import Group 
    from django.contrib.contenttypes.models import ContentType  
    try:
         new_group = Group.objects.get(name=model.nivel)
    except Exception:
        new_group = Group.objects.create(name=model.nivel)
    
    permissions = call_back(ContentType.objects.get_for_model(model) )
    for permission in permissions:                                                
        new_group.permissions.add(permission)
        model.user_permissions.add(permission)
    model.groups.add(new_group)