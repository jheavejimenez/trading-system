from django.contrib import admin

from .models import (
    Currency,
    Stock,
    Price,
    Inventory,
    Wallet,
    Trade
)

admin.site.register(Currency)
admin.site.register(Stock)
admin.site.register(Price)
admin.site.register(Inventory)
admin.site.register(Wallet)
admin.site.register(Trade)
