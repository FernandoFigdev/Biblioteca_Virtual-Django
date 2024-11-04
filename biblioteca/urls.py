from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from usuarios import views as usuario_views  # Importa as views de `usuarios`

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/usuarios/', include('usuarios.urls')),
    path('api/livros/', include('livros.urls')),
    path('api/emprestimos/', include('emprestimos.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('cadastro_usuarios/', TemplateView.as_view(template_name="cadastro_usuarios.html"), name="cadastro_usuarios"),
    path('cadastro_livros/', TemplateView.as_view(template_name="cadastro_livros.html"), name="cadastro_livros"),
    path('home_leitor/', usuario_views.home_leitor, name='home_leitor'),  # Corrigido para `usuario_views`
    path('home_admin/', usuario_views.home_admin, name='home_admin'),      # Corrigido para `usuario_views`
    path('redirect_after_login/', usuario_views.redirect_after_login, name='redirect_after_login'),  # Corrigido para `usuario_views`
]
