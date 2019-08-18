from django.db import models
from datetime import datetime

 
class Category(models.Model):
    class Meta:
        verbose_name = "カテゴリ"
        verbose_name_plural = "カテゴリ"
    
    category_name = models.CharField(max_length = 255,unique = True)
    def __str__(self):
        return self.category_name

class Stock(models.Model):
   class Meta:
       #テーブル名
       db_table ="stock"
       verbose_name ="ストック"         #追加
       verbose_name_plural ="ストック"  #追加
       
    

   #カラムの定義
   date = models.DateField(verbose_name="日付",default=datetime.now)
   money = models.IntegerField(verbose_name="残量", help_text="単位はグラム")
   category = models.CharField(verbose_name = "カテゴリ",max_length = 255,unique = True)

    