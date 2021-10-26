from django.urls import include, path
from rest_framework import routers
from . import views  #importing our view file 
from .views import StrategyCR, StrategyUpdate

router = routers.DefaultRouter()
# router.register(r'strategys', views.StrategyViewSet)


# urlpatterns = [
#     path("", views.homepage, name="home"), #mapping the homepage function
# ]

urlpatterns = [
    path('', include(router.urls)),
    path('strategy/', StrategyCR.as_view()),
    path('update-strategy/<int:strategy_id>', StrategyUpdate.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]