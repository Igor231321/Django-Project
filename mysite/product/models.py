from django.db import models

class Product(models.Model):
    product_title = models.CharField('Название товара', max_length=255)
    description = models.TextField('Описание товара')
    price = models.IntegerField('Цена товара', default=0)
    
    def __str__(self):
        return self.product_title