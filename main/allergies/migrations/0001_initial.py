# Generated by Django 2.2.2 on 2019-09-02 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='名前')),
                ('bool_0', models.NullBooleanField(default=None, verbose_name='卵アレルギー')),
                ('bool_1', models.NullBooleanField(default=None, verbose_name='乳アレルギー')),
                ('bool_2', models.NullBooleanField(default=None, verbose_name='小麦アレルギー')),
                ('bool_3', models.NullBooleanField(default=None, verbose_name='そばアレルギー')),
                ('bool_4', models.NullBooleanField(default=None, verbose_name='ピーナッツアレルギー')),
                ('bool_5', models.NullBooleanField(default=None, verbose_name='えびアレルギー')),
                ('bool_6', models.NullBooleanField(default=None, verbose_name='かにアレルギー')),
                ('bool_7', models.NullBooleanField(default=None, verbose_name='あわびアレルギー')),
                ('bool_8', models.NullBooleanField(default=None, verbose_name='大豆アレルギー')),
                ('bool_9', models.NullBooleanField(default=None, verbose_name='ごまアレルギー')),
                ('bool_10', models.NullBooleanField(default=None, verbose_name='肉アレルギー')),
                ('bool_11', models.NullBooleanField(default=None, verbose_name='くるみアレルギー')),
            ],
            options={
                'verbose_name': 'アレルギー',
                'verbose_name_plural': 'アレルギー',
                'db_table': 'allergies',
            },
        ),
    ]