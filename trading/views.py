from rest_framework import mixins, viewsets, permissions, status
from rest_framework.response import Response

from trading.models import (
    Currency,
    Stock,
    Trade,
    Wallet
)
from trading.serializer import (
    TradeSerializer,
    CurrencySerializer,
    StockSerializer,
    StockInsertSerializer,
    WalletSerializer,
    TradeInsertSerializer,
    UserPortfolioSerializer
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


class WalletView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [permissions.IsAuthenticated]
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer


class UserPortfolioView(viewsets.GenericViewSet):
    serializer_class = UserPortfolioSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(
            serializer.create(serializer.data),
            status=status.HTTP_200_OK,
        )
