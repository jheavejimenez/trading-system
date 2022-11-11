from django.contrib.auth.models import User
from django.db import models


class BaseModel(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.code


ORDERTYPE_CHOICES = (
    ('buy', 'Buy'),
    ('sell', 'Sell'),
)


class OrderType(BaseModel):
    type = models.CharField(
        max_length=4,
        choices=ORDERTYPE_CHOICES,
        default='buy',
    )


class Currency(BaseModel):

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Currency'
        verbose_name_plural = 'Currencies'


class Stock(BaseModel):
    id = models.AutoField(primary_key=True)
    currency = models.ForeignKey(
        Currency,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'


class Price(models.Model):
    stock = models.ForeignKey(
        Stock,
        on_delete=models.CASCADE,
        related_name="values",
        related_query_name="value"
    )
    currency = models.ForeignKey(
        Currency,
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    price = models.DecimalField(max_digits=7, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f'{self.stock.code} - {self.price}'

    class Meta:
        verbose_name = 'Price'
        verbose_name_plural = 'Prices'


class Inventory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'{self.stock.code} - {self.quantity}'

    class Meta:
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'{self.currency.code} - {self.balance}'

    class Meta:
        verbose_name = 'Wallet'
        verbose_name_plural = 'Wallets'


class Trade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    order_type = models.ForeignKey(OrderType, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.stock.code} - {self.quantity}'

    class Meta:
        verbose_name = 'Trade'
        verbose_name_plural = 'Trades'
