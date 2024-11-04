from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from usuarios.models import Usuario

@login_required
def redirect_after_login(request):
    perfil_usuario = Usuario.objects.get(user=request.user)
    if perfil_usuario.tipo_usuario == 'LEITOR':
        return redirect('home_leitor')
    elif perfil_usuario.tipo_usuario == 'ADMIN':
        return redirect('home_admin')
    else:
        return redirect('login')  # Caso de erro
