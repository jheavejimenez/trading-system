from django.db.models import Sum
from rest_framework import serializers

from trading.models import (
    Currency,
    Stock,
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


class BaseSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    stock = StockSerializer(read_only=True)


class WalletSerializer(BaseSerializer):
    user = UserSerializer(read_only=True)
    currency = CurrencySerializer(read_only=True)

    class Meta:
        model = Wallet
        fields = "__all__"


class TradeSerializer(BaseSerializer):
    stocks = StockSerializer(read_only=True)

    class Meta:
        model = Trade
        fields = "__all__"


class TradeInsertSerializer(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        context = kwargs.get('context', {})
        self.request = context.get('request', None)
        super().__init__(*args, **kwargs)

    class Meta:
        model = Trade
        fields = "__all__"
        read_only_fields = ['total']

    def create(self, validated_data):
        user = self.request.user
        wallet = Wallet.objects.get(user=user)
        if wallet.balance < validated_data['quantity'] * validated_data['stock'].price:
            raise serializers.ValidationError('Insufficient funds')
        wallet.balance -= validated_data['quantity'] * validated_data['stock'].price
        wallet.save()

        total_value = validated_data['quantity'] * validated_data['stock'].price
        trade = Trade.objects.create(
            user=user,
            stock=validated_data['stock'],
            quantity=validated_data['quantity'],
            total=total_value
        )
        return trade


def get_trade_info(user_id, stock):
    return {
        'total quantity': Trade.objects.filter(user=user_id, stock=stock).aggregate(Sum('quantity'))['quantity__sum'],
        'total value': Trade.objects.filter(user=user_id, stock=stock).aggregate(Sum('total'))['total__sum']
    }


class UserPortfolioSerializer(serializers.Serializer):
    stock_id = serializers.IntegerField(
        help_text="Item id for statistics",
        allow_null=True
    )

    def validate(self, attrs):
        try:
            Stock.objects.get(id=attrs['stock_id'])
        except Stock.DoesNotExist:
            if attrs['stock_id'] is not None:
                raise serializers.ValidationError('Stock does not exist')
        return attrs

    def create(self, validated_data):
        user_id = self.context.get('request').user.id
        return get_trade_info(
            user_id,
            validated_data['stock_id'],
        )
