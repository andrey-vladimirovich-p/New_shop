# Generated by Django 3.2.6 on 2022-09-24 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0002_alter_categoryproduct_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='views',
            field=models.IntegerField(default=0, verbose_name='Количество просмотров'),
        ),
    ]
