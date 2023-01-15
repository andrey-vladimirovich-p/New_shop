from django.db import models
from django.urls import reverse
from django.utils import timezone


class Product(models.Model):
    number = models.CharField(max_length=20, verbose_name="Номер", db_index=True)
    name = models.CharField(max_length=150, verbose_name="Наименование", db_index=True)
    description = models.TextField(blank=True, verbose_name='Описание')
    slug = models.SlugField(max_length=200, db_index=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name='Фото', blank=True)
    category = models.ForeignKey('CategoryProduct', on_delete=models.PROTECT, verbose_name='Категория инструмента', )
    created = models.DateTimeField(default=timezone.now, verbose_name='Дата создания')
    updated = models.DateTimeField(default=timezone.now, verbose_name='Дата обновления')
    stock = models.PositiveIntegerField(verbose_name='Доступное количество')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=False, verbose_name='Доступен')
    views = models.IntegerField(default=0, verbose_name='Просмотры')


    def __str__(self): # функция которая возвращает значение ячейки(атрибута класса News) title если мы ображаемся к классу News, а не просто адрес памяти где она записана
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail',
                       args=[self.id, self.slug])

    class Meta:
        verbose_name = 'Товар'  # название класса в ед. числе в админке
        verbose_name_plural = 'Товары'  # название класса во множественном числе
        ordering = ('name',)  # сортировка
        index_together = (('number', 'slug'),)



class CategoryProduct(models.Model):
    name = models.CharField(max_length=50, db_index=True, verbose_name='Наименование категории товаров')  # db_index -
    # это индекссация поля,
    # для более быстрого поиска в базе SQL
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    def get_absolute_url(self):  # метод для добавления абсолютного адреса сатегории с продуктами
        return reverse('categories_product', args=[self.id, self.slug])

    def __str__(self): # функция которая возвращает значение ячейки(атрибута класса News) title если мы ображаемся к классу News, а не просто адрес памяти где она записана
        return self.name

    class Meta:
        verbose_name = 'Категория товаров'
        verbose_name_plural = 'Категории товаров'
        ordering = ['name']
