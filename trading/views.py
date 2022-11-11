from rest_framework import mixins, viewsets

from trading.models import (
    Currency,
    Stock,
    Price,
    Inventory,
    Wallet,
    Trade
)
from trading.serializer import (
    TradeSerializer,
    CurrencySerializer
)


class TradingView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer


class CurrencyViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):

    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
