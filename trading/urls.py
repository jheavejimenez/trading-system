from django.urls import path, include
from rest_framework import routers

from .views import (
    TradingView,
    CurrencyViewSet
)
router = routers.DefaultRouter()
router.register(r'trading', TradingView)
router.register(r'currency', CurrencyViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
