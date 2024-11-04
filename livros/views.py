from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Livro
from .serializers import LivroSerializer

class LivroViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Livro.objects.filter(ativo=True, quantidade_disponivel__gt=0)
    serializer_class = LivroSerializer
