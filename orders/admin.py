from django.contrib import admin
from .models import Customer, Order

# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('shopify_order_id', 'customer', 'status', 'order_date', 'deadline', 'price', 'materials_cost', 'profit')
    list_filter = ('status', 'order_date', 'deadline')
    search_fields = ('shopify_order_id', 'customer__name')

admin.site.register(Customer)
admin.site.register(Order, OrderAdmin)
