from django.db import models
from datetime import datetime

 
class Stock(models.Model):
   class Meta:
       #テーブル名
       db_table ="stock"
       verbose_name ="ストック"         #追加
       verbose_name_plural ="ストック"  #追加
       
    

   #カラムの定義
   date = models.DateField(verbose_name="日付",default=datetime.now)
   money = models.IntegerField(verbose_name="残量", help_text="単位はグラム")

    