from django.contrib import admin
from cashondelivery.models import CashOnDeliveryTransaction


class CashOnDeliveryTransactionAdmin(admin.ModelAdmin):
    readonly_fields = [
        'order_number',
        'method',
        'amount',
        'currency',
        'reference',
        'date_created'
    ]

    list_display = [
        'order_number',
        'date_created',
        'amount',
        'currency',
        'confirmed',
        'date_confirmed',
    ]

    list_filter = [
        'confirmed'
    ]


admin.site.register(CashOnDeliveryTransaction, CashOnDeliveryTransactionAdmin)
