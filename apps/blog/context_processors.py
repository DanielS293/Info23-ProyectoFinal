from . import models
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User


def contexto_base(request):

    contexto = dict()

    # Acerca de
    if models.Acerca.objects.count():
        contexto['acerca'] = models.Acerca.objects.latest('creacion')
    else:
        contexto['acerca'] = ''

    # Categorias
    contexto['categorias'] = models.Categoria.objects.filter(activo=True)

    # Archivos

    contexto['archivos'] = [{'fecha':fecha} for fecha in models.Articulo.objects.dates('creacion', 'month', order='DESC').filter(publicado=True)]

    # Redes
    contexto['redes'] = models.Red.objects.all()

    return contexto

'''
    Mostrar imagen de perfil del usuario loggeado en la seccion de comentarios.
    Da error al desloggear.

    def get_avatar_usuario(request):
        id_usuario = None
        if request.user.is_authenticated:
            id_usuario = request.user.id
            #avatar = models.Perfil.objects.filter(user_id=id_usuario)
            avatar = get_object_or_404(models.Perfil, user_id=id_usuario)
            avatar = avatar.imagen
        
        return {
            'avatar' : avatar
        }
'''