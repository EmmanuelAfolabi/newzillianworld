from django.contrib import admin
from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Reply)




@admin.register(ShippingAddress)
class ShippingAddressAdmin(ImportExportModelAdmin):
    list_display = ('order', 'code', 'id', 'customer')


@admin.register(Customer)
class CustomerAdmin(ImportExportModelAdmin):
    list_display = ('name', 'phone', 'id',)

@admin.register(Receipt)
class ReceiptAdmin(ImportExportModelAdmin):
    list_display = ('id', 'uniquecode',)