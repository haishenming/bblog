# Generated by Django 2.0.2 on 2018-03-09 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_article', '0004_auto_20180309_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='article',
            name='update_time',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='修改时间'),
        ),
    ]