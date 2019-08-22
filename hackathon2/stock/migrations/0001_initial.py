# Generated by Django 2.2.2 on 2019-08-22 02:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'カテゴリ',
                'verbose_name_plural': 'カテゴリ',
            },
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.datetime.now, verbose_name='日付')),
                ('money', models.IntegerField(help_text='単位はグラム', verbose_name='残量')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='stock.Category', verbose_name='カテゴリ')),
            ],
            options={
                'verbose_name': 'ストック',
                'verbose_name_plural': 'ストック',
                'db_table': 'stock',
            },
        ),
    ]