from django.db import models

# Create your models here.
class Allergies(models.Model):
    class Meta:
        db_table = "allergies"
        verbose_name = "アレルギー"
        verbose_name_plural = "アレルギー"
    name = models.CharField(verbose_name = "名前",max_length = 500)
    bool_0 = models.NullBooleanField(
        verbose_name='卵アレルギー',
        default=None,
    )
    bool_1 = models.NullBooleanField(
        verbose_name='乳アレルギー',
        default=None,
    )
    bool_2 = models.NullBooleanField(
        verbose_name='小麦アレルギー',
        default=None,
    )
    bool_3 = models.NullBooleanField(
        verbose_name='そばアレルギー',
        default=None,
    )
    bool_4 = models.NullBooleanField(
        verbose_name='ピーナッツアレルギー',
        default=None,
    )
    bool_5 = models.NullBooleanField(
        verbose_name='えびアレルギー',
        default=None,
    )
    bool_6 = models.NullBooleanField(
        verbose_name='かにアレルギー',
        default=None,
    )
    bool_7 = models.NullBooleanField(
        verbose_name='あわびアレルギー',
        default=None,
    )
    bool_8 = models.NullBooleanField(
        verbose_name='大豆アレルギー',
        default=None,
    )
    bool_9 = models.NullBooleanField(
        verbose_name='ごまアレルギー',
        default=None,
    )
    bool_10 = models.NullBooleanField(
        verbose_name='肉アレルギー',
        default=None,
    )
    bool_11 = models.NullBooleanField(
        verbose_name='くるみアレルギー',
        default=None,
    )