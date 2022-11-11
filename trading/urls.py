from rest_framework import routers

from .views import (
    TradingView,
    CurrencyView,
    StockView,
    WalletView,
    UserPortfolioView

)

router = routers.DefaultRouter()
router.register(r'trade', TradingView)
router.register(r'currency', CurrencyView)
router.register(r'stock', StockView)
router.register(r'wallet', WalletView)
router.register(r'portfolio', UserPortfolioView, basename='portfolio')

urlpatterns = router.urls
