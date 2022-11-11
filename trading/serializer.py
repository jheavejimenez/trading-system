from rest_framework import serializers

from trading.models import (
    Currency,
    Stock,
    Price,
    Inventory,
    Wallet,
    Trade,
    User
)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = "__all__"


class StockSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer(read_only=True)

    class Meta:
        model = Stock
        fields = "__all__"


class StockInsertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class PriceSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)

    class Meta:
        model = Price
        fields = "__all__"


class BaseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    stock = StockSerializer(read_only=True)


class InventorySerializer(BaseSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class WalletSerializer(BaseSerializer):
    user = UserSerializer(read_only=True)
    currency = CurrencySerializer(read_only=True)

    class Meta:
        model = Wallet
        fields = "__all__"


class TradeSerializer(BaseSerializer):
    stock = StockSerializer(read_only=True)

    class Meta:
        model = Trade
        fields = "__all__"
