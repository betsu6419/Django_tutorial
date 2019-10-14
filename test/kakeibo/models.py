from django.db import models
from django.urls import reverse
from datetime import datetime 
# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "category"
        verbose_name = 'カテゴリ'
        verbose_name_plural = 'カテゴリ'
    category_name = models.CharField(max_length = 255,unique = True)

    def __str__(self):
        return self.category_name

class Kakeibo(models.Model):
    class Meta:
        db_table = "kakeibo"
        verbose_name = '家計簿'
        verbose_name_plural = '家計簿'
    date = models.DateField(verbose_name = '日付',default = datetime.now)
    category = models.ForeignKey(Category,on_delete = models.PROTECT,verbose_name = "カテゴリ")
    money = models.IntegerField(verbose_name="金額",help_text="単位は日本円")
    memo = models.CharField(verbose_name="メモ",max_length = 500)
    result = models.CharField(verbose_name="高いかやすいか",max_length = 500)
    def __str__(self):
        return self.memo
    
class Location(models.Model):
    class Meta:
        db_table = 'location'
    name = models.CharField(verbose_name='ロケーション名', max_length=255)
    memo = models.CharField(verbose_name='メモ', max_length=255, default='', blank=True)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    def __str__(self):
        return self.name
    @staticmethod
    def get_absolute_url(self):
        return reverse('monitor:index')

class WeatherData(models.Model):
    """気象データモデル"""
    class Meta:
        db_table = 'weather_data'
        unique_together = (('location', 'data_datetime'),)
    location = models.ForeignKey(Location,verbose_name='ロケーション', on_delete=models.PROTECT)
    data_datetime = models.DateTimeField(verbose_name='データ日時', default=datetime.strptime('2001-01-01 00:00:00', '%Y-%m-%d %H:%M:%S'))
    temperature = models.FloatField(verbose_name='気温')
    humidity = models.FloatField(verbose_name='湿度')
    created_at = models.DateTimeField(verbose_name='登録日時', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='更新日時', auto_now=True)
    def __str__(self):
        return self.location.name + ":" + str(self.data_datetime)