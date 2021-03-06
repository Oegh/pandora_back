from rest_framework import serializers
from .models import Strategy

class StrategySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Strategy
        fields = ('id', 'name', 'description')