from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['book']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email',
                    'address', 'city', 'paid',
                    'created', 'updated', 'status']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]
    actions = ["change_status_to_paid"]

    def change_status_to_paid(self, request, queryset):
        queryset.update(paid=True)

    change_status_to_paid.short_description = "Status: paid"


admin.site.register(Order, OrderAdmin)
