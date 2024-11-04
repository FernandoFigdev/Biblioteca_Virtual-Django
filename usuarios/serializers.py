from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

    def validate_email(self, value):
        # Verifica se já existe um usuário com este email
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este email já está cadastrado.")
        return value

    def create(self, validated_data):
        # Remove a senha do validated_data antes de criar o usuário
        senha = validated_data.pop('senha')
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=senha
        )
        # Cria o perfil de usuário
        usuario = Usuario.objects.create(user=user, **validated_data)
        return usuario
