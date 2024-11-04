from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    isbn = models.CharField(max_length=13, unique=True)
    editora = models.CharField(max_length=255)
    ano_publicacao = models.PositiveIntegerField()
    genero = models.CharField(max_length=50)
    quantidade_total = models.PositiveIntegerField()
    quantidade_disponivel = models.PositiveIntegerField()
    descricao = models.TextField(blank=True, null=True)
    ativo = models.BooleanField(default=True)  # Novo campo para ativar/inativar livro

    def __str__(self):
        return f"{self.titulo} - {self.autor}"
