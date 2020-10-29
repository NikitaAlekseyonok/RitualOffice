from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
import re


class Client(models.Model):
    clientID = models.AutoField(primary_key=True, verbose_name='ID')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    deceased_surname = models.CharField(max_length=30, verbose_name='Фамилия усопшего')
    deceased_name = models.CharField(max_length=30, verbose_name='Имя усопшего')
    deceased_patronymic = models.CharField(max_length=30, verbose_name='Отчество усопшего')
    phoneNumber = models.IntegerField(verbose_name='Телефон')

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return "{} {}".format(self.surname, self.name)

    def get_absolute_url(self):
        return reverse('view_client', kwargs={'pk': self.clientID})

    def clean_name(self):
        name = self.cleaned_data['name']
        if re.search('\d', name):
            raise ValidationError('Ошибка')
        return name


class Services(models.Model):
    servicesID = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=30, verbose_name='Название услуги')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name


class Hall(models.Model):
    hallID = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=30, verbose_name='Название')
    servicesID = models.ForeignKey('Services', on_delete=models.PROTECT)
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Зал'
        verbose_name_plural = 'Залы'

    def __str__(self):
        return self.name


class Discount(models.Model):
    discountID = models.AutoField(primary_key=True, verbose_name='ID')
    servicesID = models.ForeignKey('Services', on_delete=models.PROTECT)
    description = models.TextField(verbose_name='Описание')
    discountAmount = models.IntegerField(verbose_name='Сумма скидки')

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return "{}".format(self.discountID)


class Position(models.Model):
    positionID = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=30, verbose_name='Наименование')
    salary = models.IntegerField(verbose_name='Зарпалата')

    class Meta:
        verbose_name = 'Должность'
        verbose_name_plural = 'Должности'

    def __str__(self):
        return self.name


class Worker(models.Model):
    workerID = models.AutoField(primary_key=True, verbose_name='ID')
    surname = models.CharField(max_length=30, verbose_name='Фамилия')
    name = models.CharField(max_length=30, verbose_name='Имя')
    patronymic = models.CharField(max_length=30, verbose_name='Отчество')
    positionID = models.ForeignKey('Position', on_delete=models.PROTECT)
    hallID = models.ForeignKey('Hall', on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'

    def __str__(self):
        return "{} {}".format(self.surname, self.name)


class Order(models.Model):
    orderID = models.AutoField(primary_key=True)
    clientID = models.ForeignKey('Client', on_delete=models.PROTECT, verbose_name='Клиент')
    workerID = models.ForeignKey('Worker', on_delete=models.PROTECT, verbose_name='Работник')
    hallID = models.ForeignKey('Hall', on_delete=models.PROTECT, verbose_name='Зал')
    servicesID = models.ForeignKey('Services', on_delete=models.PROTECT, verbose_name='Услуга')
    discountID = models.ForeignKey('Discount', on_delete=models.PROTECT, verbose_name='Скидка')
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    is_paid = models.BooleanField(verbose_name='Подтверждение оплаты', )

    class Meta:
        verbose_name = 'Отчёт'
        verbose_name_plural = 'Отчёты'

    def get_absolute_url(self):
        return reverse('view_order', kwargs={'pk': self.orderID})

    def calculate_sum(self):
        return self.hallID.price + self.workerID.positionID.salary / 10 + self.servicesID.price - self.discountID.discountAmount

    def __str__(self):
        return "{}".format(self.clientID)


class ProductType(models.Model):
    productTypeID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, verbose_name='Тип товара')

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товара'

    def get_absolute_url(self):
        return reverse('view_productType', kwargs={'pk': self.productTypeID})

    def __str__(self):
        return self.name


class Product(models.Model):
    productID = models.AutoField(primary_key=True, verbose_name='ID')
    name = models.CharField(max_length=30, verbose_name='Название товара')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True)
    productTypeID = models.ForeignKey('ProductType', on_delete=models.PROTECT)
    discountID = models.ForeignKey('ProductDiscounts', on_delete=models.PROTECT)
    price = models.IntegerField(verbose_name='Цена')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def get_absolute_url(self):
        return reverse('view_product', kwargs={'pk': self.productID})

    def __str__(self):
        return self.name


class ProductOrder(models.Model):
    productOrderID = models.AutoField(primary_key=True, verbose_name='ID')
    clientID = models.ForeignKey('Client', on_delete=models.PROTECT)
    productID = models.ForeignKey('Product', on_delete=models.PROTECT)
    discountID = models.ForeignKey('ProductDiscounts', on_delete=models.PROTECT)
    date = models.DateField(verbose_name='Дата')
    time = models.TimeField(verbose_name='Время')
    is_paid = models.BooleanField(verbose_name='Подтверждение оплаты')

    class Meta:
        verbose_name = 'Заказ товара'
        verbose_name_plural = 'Заказы товара'

    def get_absolute_url(self):
        return reverse('view_productorder', kwargs={'pk': self.productOrderID})

    def calculate_sum(self):
        return self.productID.price - self.discountID.discountAmount

    def __str__(self):
        return "{}".format(self.clientID)


class ProductDiscounts(models.Model):
    discountID = models.AutoField(primary_key=True, verbose_name='ID')
    description = models.TextField(verbose_name='Описание')
    discountAmount = models.IntegerField(verbose_name='Сумма скидки')

    class Meta:
        verbose_name = 'Скидка на товары'
        verbose_name_plural = 'Скидки на товары'

    def __str__(self):
        return self.description
