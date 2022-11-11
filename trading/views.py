from rest_framework import mixins, viewsets

from trading.models import (
    Currency,
    Stock,
    Price,
    Inventory,
    Wallet,
    Trade
)
from trading.serializer import TradeSerializer


class TradingView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer
