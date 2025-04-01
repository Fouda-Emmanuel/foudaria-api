from django.contrib import admin
from .models import Order

# Register your models here.
admin.site.site_header = "FOUDARIA API"
admin.site.site_title = "PORTAL"  
admin.site.index_title = "ADMINISTRATION"  

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'order_id', 'car', 'quantity', 'price', 'order_status', 'payment_method', 'created_at']
    readonly_fields = ('price', 'order_id',) 
    


