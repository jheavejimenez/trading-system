from django.urls import path, include
from rest_framework import routers

from .views import (
    TradingView,
    CurrencyView,
    StockView,
    InventoryView,
    WalletView
)

router = routers.DefaultRouter()
router.register(r'trade', TradingView)
router.register(r'currency', CurrencyView)
router.register(r'stock', StockView)
router.register(r'inventory', InventoryView)
router.register(r'wallet', WalletView)

urlpatterns = router.urls
