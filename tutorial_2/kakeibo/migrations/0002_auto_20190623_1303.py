# Generated by Django 2.2.2 on 2019-06-23 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kakeibo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'カテゴリ', 'verbose_name_plural': 'カテゴリ'},
        ),
        migrations.AlterModelOptions(
            name='kakeibo',
            options={'verbose_name': '家計簿', 'verbose_name_plural': '家計簿'},
        ),
        migrations.AddField(
            model_name='kakeibo',
            name='result',
            field=models.CharField(default=None, max_length=500, verbose_name='高いかやすいか'),
        ),
    ]
