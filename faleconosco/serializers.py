from rest_framework import serializers

from .models import Contato


class ContatoSerializer(serializers.ModelSerializer):
    documento = serializers.FileField(read_only=True)

    class Meta:
        model = Contato
        fields = ['id', 'nome', 'email', 'telefone', 'documento', 'mensagem', 'criado_em']
