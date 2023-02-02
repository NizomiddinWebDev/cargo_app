from django.contrib import admin

# Register your models here.
from app.models import Client, Product, Mark


class ProductdAdmin(admin.ModelAdmin):
    list_filter = ('created_date',)
    list_display = ['name', 'product_count', 'price', 'created_date', 'client']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['tg_id', 'full_name', 'prop_address', 'passport', 'mark', 'phone']


admin.site.register(Client, ClientAdmin)
admin.site.register(Product, ProductdAdmin)
admin.site.register(Mark)
