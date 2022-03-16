from django.contrib import admin
from .models import Order, StatusCRM, CommentCRM

# Register your models here.
admin.site.register(Order)
admin.site.register(StatusCRM)
admin.site.register(CommentCRM)