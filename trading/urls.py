from django.urls import path, include
from rest_framework import routers

from .views import (
    TradingView,
    CurrencyView,
    StockView,
    PriceView,
    InventoryView,
    WalletView
)

router = routers.DefaultRouter()
router.register(r'trading', TradingView)
router.register(r'currency', CurrencyView)
router.register(r'stock', StockView)
router.register(r'price', PriceView)
router.register(r'inventory', InventoryView)
router.register(r'wallet', WalletView)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
