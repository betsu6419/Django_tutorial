# Generated by Django 2.2.2 on 2019-08-18 08:47

from django.db import migrations


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
    ]