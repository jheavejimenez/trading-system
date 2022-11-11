from django.contrib import admin

from .models import (
    Currency,
    Stock,
    Wallet,
    Trade
)

admin.site.register(Currency)
admin.site.register(Stock)
admin.site.register(Wallet)
admin.site.register(Trade)
