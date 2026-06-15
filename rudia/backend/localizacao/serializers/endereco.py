from rest_framework import serializers
from localizacao.models import Endereco
import re


class EnderecoSerializer(serializers.ModelSerializer):
    """Serializer para Endereço"""
    endereco_completo = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Endereco
        fields = [
            'id',
            'cep',
            'logradouro',
            'numero',
            'complemento',
            'endereco_completo'
        ]
        read_only_fields = ['id']
    
    def get_endereco_completo(self, obj):
        """Retorna o endereço formatado completo"""
        endereco = f"{obj.logradouro}, {obj.numero}"
        if obj.complemento:
            endereco += f" - {obj.complemento}"
        endereco += f" - CEP: {self.format_cep(obj.cep)}"
        return endereco
    
    @staticmethod
    def format_cep(cep):
        """Formata CEP para exibição (12345678 -> 12345-678)"""
        if len(cep) == 8 and cep.isdigit():
            return f"{cep[:5]}-{cep[5:]}"
        return cep
    
    def validate_cep(self, value):
        """Valida e normaliza o CEP (remove formatação)"""
        # Remove caracteres não numéricos
        cep = re.sub(r'\D', '', value)
        
        if len(cep) != 8:
            raise serializers.ValidationError("CEP deve conter 8 dígitos.")
        
        return cep
    
    def validate_numero(self, value):
        """Valida o número do endereço"""
        numero = value.strip().upper()
        
        if not numero:
            raise serializers.ValidationError("Número é obrigatório.")
        
        # Aceita números ou 'S/N' para sem número
        if numero not in ['S/N', 'SN'] and not any(char.isdigit() for char in numero):
            raise serializers.ValidationError("Número deve conter dígitos ou ser 'S/N'.")
        
        return numero
    
    def validate_logradouro(self, value):
        """Normaliza o logradouro"""
        return value.strip().title()
    
    def validate(self, attrs):
        """Valida se já existe endereço com mesmo logradouro e número"""
        logradouro = attrs.get('logradouro')
        numero = attrs.get('numero')
        
        # Se for atualização, exclui a própria instância da validação
        instance = self.instance
        query = Endereco.objects.filter(logradouro=logradouro, numero=numero)
        
        if instance:
            query = query.exclude(pk=instance.pk)
        
        if query.exists():
            raise serializers.ValidationError({
                'endereco': f'Já existe um endereço cadastrado em {logradouro}, {numero}.'
            })
        
        return attrs


class EnderecoResumoSerializer(serializers.ModelSerializer):
    """Serializer resumido de Endereço (para uso em nested serializers)"""
    endereco_completo = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Endereco
        fields = ['id', 'endereco_completo']
        read_only_fields = ['id']
    
    def get_endereco_completo(self, obj):
        """Retorna o endereço formatado completo"""
        endereco = f"{obj.logradouro}, {obj.numero}"
        if obj.complemento:
            endereco += f" - {obj.complemento}"
        return endereco