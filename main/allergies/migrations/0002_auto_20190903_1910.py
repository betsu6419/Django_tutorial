# Generated by Django 2.2.2 on 2019-09-03 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allergies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergies',
            name='name',
            field=models.CharField(max_length=500, unique=True, verbose_name='名前'),
        ),
    ]