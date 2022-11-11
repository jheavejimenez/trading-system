from rest_framework import mixins, viewsets

from trading.models import (
    Currency,
    Stock,
    Trade
)
from trading.serializer import (
    TradeSerializer,
    CurrencySerializer, StockSerializer, StockInsertSerializer
)


class TradingView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Trade.objects.all()
    serializer_class = TradeSerializer


class CurrencyView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class StockView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Stock.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return StockInsertSerializer
        return StockSerializer
