from django.urls import path, include
from rest_framework import routers

from .views import (
    TradingView,
    CurrencyView, StockView
)
router = routers.DefaultRouter()
router.register(r'trading', TradingView)
router.register(r'currency', CurrencyView)
router.register(r'stock', StockView)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
