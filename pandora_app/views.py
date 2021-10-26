from django.shortcuts import render

from rest_framework import viewsets

from .serializers import StrategySerializer
from .models import Strategy

# Create your views here.

class StrategyViewSet(viewsets.ModelViewSet):
    queryset = Strategy.objects.all().order_by('id')
    serializer_class = StrategySerializer

def homepage(request):
    return render(request, 'index.html', context={})

