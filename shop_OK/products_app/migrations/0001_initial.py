# Generated by Django 4.0.1 on 2022-01-21 09:15

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50, verbose_name='Наименование категории инструмента')),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name': 'Категория инструмента',
                'verbose_name_plural': 'Категории инструмента',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(db_index=True, max_length=20, verbose_name='Номер')),
                ('name', models.CharField(db_index=True, max_length=150, verbose_name='Наименование')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('slug', models.SlugField(max_length=200)),
                ('check_date', models.DateField(verbose_name='Дата поверки')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/', verbose_name='Фото')),
                ('available', models.BooleanField(default=False, verbose_name='Доступен')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата создания')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата обновления')),
                ('stock', models.PositiveIntegerField(verbose_name='Доступное количество')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products_app.categoryproduct', verbose_name='Категория инструмента')),
            ],
            options={
                'verbose_name': 'Инструмент',
                'verbose_name_plural': 'Инструменты',
                'ordering': ('name',),
                'index_together': {('number', 'slug')},
            },
        ),
    ]
