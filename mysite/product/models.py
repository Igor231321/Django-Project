from django.db import models


class Product(models.Model):
    title = models.CharField('Название товара', max_length=50)
    amount = models.IntegerField('Цена товара', default=0)
    description = models.TextField('Описание товара')


    def __str__(self):
        return self.title
