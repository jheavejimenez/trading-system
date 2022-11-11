from rest_framework import mixins, viewsets, permissions

from trading.models import (
    Currency,
    Stock,
    Trade,
    Inventory,
    Wallet
)
from trading.serializer import (
    TradeSerializer,
    CurrencySerializer,
    StockSerializer,
    StockInsertSerializer,
    InventorySerializer,
    WalletSerializer,
    TradeInsertSerializer
)


class TradingView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Trade.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return TradeInsertSerializer
        return TradeSerializer


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


class InventoryView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class WalletView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
