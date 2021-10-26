from django.db import models

# Create your models here.

class Strategy(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.name

class SpecificStrategyInst(models.Model):
    description = models.CharField(max_length= 200)
    strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE)
    def __str__(self):
        return self.description
