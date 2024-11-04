from django.db import models
from django.utils import timezone
from usuarios.models import Usuario
from livros.models import Livro

class Emprestimo(models.Model):
    STATUS_EMPRESTIMO = [
    ('PENDENTE', 'Pendente'),
    ('APROVADO', 'Aprovado'),
    ('REJEITADO', 'Rejeitado'),
    ]

    status = models.CharField(max_length=10, choices=STATUS_EMPRESTIMO, default='PENDENTE')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(default=timezone.now)
    data_devolucao_prevista = models.DateField()
    data_devolucao = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_EMPRESTIMO, default='ABERTO')

    def __str__(self):
        return f"Empréstimo de {self.livro} para {self.usuario}"
