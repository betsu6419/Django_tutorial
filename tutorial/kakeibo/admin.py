from django.contrib import admin

# Register your models here.

from .models import Category,Kakeibo
admin.site.register(Category)
admin.site.register(Kakeibo)