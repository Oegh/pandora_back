from django.contrib import admin
from .models import Strategy
from .models import SpecificStrategyInst

# Register your models here.

admin.site.register(Strategy)
admin.site.register(SpecificStrategyInst)

