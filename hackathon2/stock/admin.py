import csv
from django.contrib import admin
from django.core.files.storage import default_storage

storage = default_storage
storage.location = 'stock/'

# Register your models here.
from .models import Stock,Category

csv_file = storage.open("shampweight.csv","r")
f = csv.reader(csv_file)
for row in f:
    days = row[0].replace("/","-")
    day = days[:5] + "0" + days[5:]
    b = Stock(date = day,money = row[1],category = row[2])
    b.save()
csv_file.close()

class StockAdmin(admin.ModelAdmin):
    list_display=('category','date','money')



admin.site.register(Stock,StockAdmin) 
admin.site.register(Category) 
