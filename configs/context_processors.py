from usuarios.models import Notificaciones, Usuario

def notificaciones(request):
    if request.user.is_authenticated:
        notificaciones = Notificaciones.objects.filter(user=request.user, leido=False)
        return {'notificaciones': notificaciones}
    return {'notificaciones': []}
