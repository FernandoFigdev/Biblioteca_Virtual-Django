from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Usuario
from .serializers import UsuarioSerializer
from emprestimos.models import Emprestimo
from livros.models import Livro

class UsuarioViewSet(ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        # Cria o usuário padrão do Django
        user = User.objects.create_user(
            username=request.data['email'],
            email=request.data['email'],
            password=request.data['senha']
        )
        
        # Cria o perfil de usuário relacionado
        usuario = Usuario.objects.create(
            user=user,
            nome_completo=request.data['nome_completo'],
            tipo_usuario=request.data['tipo_usuario'],
            endereco=request.data.get('endereco', ''),
            telefone=request.data.get('telefone', '')
        )
        
        serializer = self.get_serializer(usuario)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

@login_required
def redirect_after_login(request):
    try:
        perfil_usuario = Usuario.objects.get(user=request.user)
    except Usuario.DoesNotExist:
        return redirect('login')  # Redireciona para login se o perfil não for encontrado

    if perfil_usuario.tipo_usuario == 'LEITOR':
        return redirect('home_leitor')
    elif perfil_usuario.tipo_usuario == 'ADMIN':
        return redirect('home_admin')
    else:
        return redirect('login')

@login_required
def home_leitor(request):
    perfil_usuario = Usuario.objects.get(user=request.user)
    livros_disponiveis = Livro.objects.filter(ativo=True, quantidade_disponivel__gt=0)
    historico_emprestimos = Emprestimo.objects.filter(usuario=perfil_usuario)

    context = {
        'livros_disponiveis': livros_disponiveis,
        'historico_emprestimos': historico_emprestimos,
    }
    return render(request, 'home_leitor.html', context)

@login_required
def home_admin(request):
    # Obtém todos os livros e apenas os empréstimos pendentes para o administrador
    livros = Livro.objects.all()
    emprestimos_pendentes = Emprestimo.objects.filter(status='PENDENTE')

    context = {
        'livros': livros,
        'emprestimos_pendentes': emprestimos_pendentes,
    }
    return render(request, 'home_admin.html', context)