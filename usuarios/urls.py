from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsuarioViewSet
from . import views

router = DefaultRouter()
router.register(r'', UsuarioViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('home_leitor/', views.home_leitor, name='home_leitor'),
    path('home_admin/', views.home_admin, name='home_admin'),
    path('redirect_after_login/', views.redirect_after_login, name='redirect_after_login'),
]
