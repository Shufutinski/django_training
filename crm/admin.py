from django.contrib import admin
from .models import Order, StatusCRM, CommentCRM

# Register your models here.
class OrderAdm(admin.ModelAdmin):

    list_display = ('id', 'order_status', 'order_name', 'order_phone', 'order_dt')
    list_display_links = ('id', 'order_name')
    search_fields = ('id', 'order_name', 'order_phone', 'order_dt')
    list_filter = ('order_status',)
    list_editable = ('order_status', 'order_phone')


admin.site.register(Order, OrderAdm)
admin.site.register(StatusCRM)
admin.site.register(CommentCRM)