from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.exceptions import ValidationError
from django.db.models import Q
from .models import Emprestimo
from .serializers import EmprestimoSerializer
from livros.models import Livro
from usuarios.models import Usuario
from rest_framework.decorators import action
from rest_framework import status

class EmprestimoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Emprestimo.objects.all()
    serializer_class = EmprestimoSerializer

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def aprovar(self, request, pk=None):
        emprestimo = self.get_object()

        # Verifica se o status está PENDENTE antes de aprovar
        if emprestimo.status != 'PENDENTE':
            return Response({'detail': 'Empréstimo não está pendente.'}, status=status.HTTP_400_BAD_REQUEST)

        # Reduz a quantidade disponível do livro e altera o status para APROVADO
        if emprestimo.livro.quantidade_disponivel > 0:
            emprestimo.livro.quantidade_disponivel -= 1
            emprestimo.livro.save()
            emprestimo.status = 'APROVADO'
            emprestimo.save()
            return Response({'detail': 'Empréstimo aprovado com sucesso.'}, status=status.HTTP_200_OK)
        else:
            return Response({'detail': 'Livro indisponível para empréstimo.'}, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def concluir(self, request, pk=None):
        emprestimo = self.get_object()

        # Verifica se o status está APROVADO antes de concluir
        if emprestimo.status != 'APROVADO':
            return Response({'detail': 'Empréstimo não está aprovado.'}, status=status.HTTP_400_BAD_REQUEST)

        # Incrementa a quantidade disponível do livro e altera o status para CONCLUIDO
        emprestimo.livro.quantidade_disponivel += 1
        emprestimo.livro.save()
        emprestimo.status = 'CONCLUIDO'
        emprestimo.save()
        return Response({'detail': 'Empréstimo concluído com sucesso.'}, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        usuario = self.request.user
        perfil_usuario = Usuario.objects.filter(user=usuario).first()
        if not perfil_usuario:
            raise ValidationError("Usuário não possui um perfil válido no sistema.")
        
        if perfil_usuario.tipo_usuario != 'LEITOR':
            raise ValidationError("Apenas usuários do tipo Leitor podem solicitar empréstimos.")
        
        livro = serializer.validated_data['livro']
        if livro.quantidade_disponivel <= 0:
            raise ValidationError("Este livro não está disponível para empréstimo.")

        # Cria a solicitação de empréstimo com status "PENDENTE"
        emprestimo = serializer.save(usuario=perfil_usuario, status='PENDENTE')
        print("Solicitação de empréstimo criada com status PENDENTE.")

    def perform_update(self, serializer):
        emprestimo = serializer.save()
        if emprestimo.status == 'CONCLUIDO' and emprestimo.data_devolucao:
            emprestimo.livro.quantidade_disponivel += 1
            emprestimo.livro.save()

    @action(detail=False, methods=['get'], permission_classes=[IsAuthenticated])
    def historico(self, request):
        usuario = request.user
        historico = Emprestimo.objects.filter(usuario=usuario)
        serializer = self.get_serializer(historico, many=True)
        return Response(serializer.data)

class RelatorioEmprestimosView(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        data_inicial = request.query_params.get('data_inicial')
        data_final = request.query_params.get('data_final')

        queryset = Emprestimo.objects.all()
        if data_inicial and data_final:
            queryset = queryset.filter(
                Q(data_emprestimo__range=[data_inicial, data_final]) |
                Q(data_devolucao__range=[data_inicial, data_final])
            )

        serializer = EmprestimoSerializer(queryset, many=True)
        return Response(serializer.data)
