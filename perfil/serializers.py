# todo/todo_api/serializers.py
from rest_framework import serializers
from .models import Perfil

class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = [ 'usuario', 'idade', 'data_nascimento', 'cpf', 'endereco', 'numero', 'complemento', 'bairro', 'cep', 'cidade', 'estado']

