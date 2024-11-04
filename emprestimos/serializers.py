from rest_framework import serializers
from .models import Emprestimo

class EmprestimoSerializer(serializers.ModelSerializer):
    # Ajuste para DateField diretamente
    data_devolucao_prevista = serializers.DateField()
    data_devolucao = serializers.DateField(allow_null=True)

    class Meta:
        model = Emprestimo
        fields = '__all__'
