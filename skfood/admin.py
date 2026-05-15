from django.contrib import admin
from .models import FoodOrder

@admin.register(FoodOrder)
class FoodOrderAdmin(admin.ModelAdmin):
    list_display = (
        'order_id',
        'customer_name',
        'food_item',
        'quantity',
        'price',
        'delivery_address',
        'order_status'
    )