from django.db import models
from datetime import datetime
# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "category"
    category_name = models.CharField(max_length = 255,unique = True)

class Kakeibo(models.Model):
    class Meta:
        db_table = "kakeibo"
    date = models.DateField(verbose_name = '日付',default = datetime.now)
    category = models.ForeignKey(Category,on_delete = models.PROTECT,verbose_name = "カテゴリ")
    money = models.IntegerField(verbose_name="金額",help_text="単位は日本円")
    memo = models.CharField(verbose_name="メモ",max_length = 500)