from rest_framework import serializers
from servicos.models import Tag


class TagSerializer(serializers.ModelSerializer):
    """Serializer para Tags"""
    
    class Meta:
        model = Tag
        fields = ['id', 'nome']
        read_only_fields = ['id']
