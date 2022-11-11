from rest_framework import mixins, viewsets, permissions

from trading.models import (
    Currency,
    Stock,
    Trade,
    Price,
    Inventory,
    Wallet
)
from trading.serializer import (
    TradeSerializer,
    CurrencySerializer,
    StockSerializer,
    StockInsertSerializer,
    PriceSerializer,
    InventorySerializer, WalletSerializer
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


class PriceView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Price.objects.all()
    serializer_class = PriceSerializer


class InventoryView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class WalletView(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = (permissions.IsAdminUser,)
