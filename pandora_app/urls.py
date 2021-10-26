from django.urls import include, path
from rest_framework import routers
from . import views  #importing our view file 

router = routers.DefaultRouter()
router.register(r'strategy', views.StrategyViewSet)


# urlpatterns = [
#     path("", views.homepage, name="home"), #mapping the homepage function
# ]

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]