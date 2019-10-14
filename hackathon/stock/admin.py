import csv
from django.contrib import admin
from django.core.files.storage import default_storage

storage = default_storage
storage.location = 'stock/'

# Register your models here.
from .models import Stock


class StockAdmin(admin.ModelAdmin):
    list_display=('date','money')



admin.site.register(Stock,StockAdmin) 