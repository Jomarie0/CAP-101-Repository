from django.contrib import admin
from .models import PurchaseOrder

class PurchaseOrderAdmin(admin.ModelAdmin):
    list_display = ('purchase_order_id', 'supplier', 'created_by', 'status', 'created_at', 'total_cost')
    search_fields = ('purchase_order_id', 'supplier__name')
    list_filter = ('status',)

admin.site.register(PurchaseOrder, PurchaseOrderAdmin)
