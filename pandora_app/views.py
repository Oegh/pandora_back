from django.shortcuts import render

from rest_framework import viewsets

from .serializers import StrategySerializer
from .models import Strategy

from django.http import JsonResponse
import json

from django.views import View

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

# class StrategyViewSet(viewsets.ModelViewSet):
#     queryset = Strategy.objects.all().order_by('id')
#     serializer_class = StrategySerializer

@method_decorator(csrf_exempt, name='dispatch')
class StrategyCR(View):
    def get(self, request):
        items_count = Strategy.objects.count()
        items = Strategy.objects.all()

        items_data = []
        for item in items:
            items_data.append({
                'id': item.pk,
                'name': item.name,
                'description': item.description,
            })

        data = {
            'items': items_data,
            'count': items_count,
        }

        return JsonResponse(data)
    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        d_name = data.get('strategy_name')
        d_desc = data.get('strategy_desc')

        strategy_data = {
            'name': d_name,
            'description': d_desc,
        }

        strategy_item = Strategy.objects.create(**strategy_data)

        data = {
            "message": f"New Strategy added: {strategy_item.id}"
        }
        return JsonResponse(data, status=201) 

@method_decorator(csrf_exempt, name='dispatch')
class StrategyUpdate(View):
    def patch(self, request, strategy_id):
        data = json.loads(request.body.decode("utf-8"))

        item = Strategy.objects.get(id=strategy_id)
        item.name = data['strategy_name']
        item.desc = data['strategy_desc']
        item.save()

        data = {
            'message': f'Strategy {strategy_id} has been updated'
        }

        return JsonResponse(data)
    def delete(self, request, strategy_id):
        item = Strategy.objects.get(id=strategy_id)
        item.delete()

        data = {
            'message': f'Strategy {strategy_id} has been deleted'
        }

        return JsonResponse(data)

def homepage(request):
    return render(request, 'index.html', context={})

