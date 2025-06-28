from api.models import Servidor, Cargo, Departamento, Vinculo, Ponto
from rest_framework import serializers
from django.utils import timezone

class ServidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Servidor
        fields = '__all__'

class CargoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'

class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'

class VinculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vinculo
        fields = '__all__'

class PontoSerializer(serializers.ModelSerializer):
    servidor_nome = serializers.CharField(source='servidor.nome_servidor', read_only=True)
    tipo_ponto_display = serializers.CharField(source='get_tipo_ponto_display', read_only=True)

    class Meta:
        model = Ponto
        fields = [
            'id_ponto', 
            'servidor',
            'servidor_nome',
            'tipo_ponto',
            'tipo_ponto_display',
            'data_hora', 
            'latitude', 
            'longitude'
        ]
        
        read_only_fields = ['id_ponto', 'servidor', 'tipo_ponto', 'data_hora']

    def create(self, validated_data):
        servidor = self.context['request'].user
        
        hoje = timezone.localtime(timezone.now()).date()
        ultimo_ponto = Ponto.objects.filter(
            servidor=servidor, 
            data_hora__date=hoje
        ).order_by('-data_hora').first()

        tipo_ponto_novo = '2' if ultimo_ponto and ultimo_ponto.tipo_ponto == '1' else '1'
            
        ponto = Ponto.objects.create(
            servidor=servidor,
            tipo_ponto=tipo_ponto_novo,
            **validated_data
        )
        return ponto