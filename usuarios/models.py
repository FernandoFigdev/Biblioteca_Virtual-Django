from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True, blank=True)  # Relacionamento com User
    TIPOS_USUARIO = [
        ('ADMIN', 'Administrador'),
        ('LEITOR', 'Leitor'),
    ]

    nome_completo = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    tipo_usuario = models.CharField(max_length=10, choices=TIPOS_USUARIO, default='LEITOR')
    endereco = models.TextField(blank=True, null=True)
    telefone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"{self.nome_completo} ({self.tipo_usuario})"
