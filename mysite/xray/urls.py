from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'xray', views.XrayView)

urlpatterns = [
    path('', views.index, name='index'),
    path('archive', views.archive, name='archive'),
    path('result', views.result, name='result'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]