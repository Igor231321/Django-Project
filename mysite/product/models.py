from django.db import models
from django.urls import reverse


class Product(models.Model):
    product_title = models.CharField('Название товара', max_length=255)
    slug = models.SlugField("Короткая метка", max_length=255, blank=True, unique=True, db_index=True)
    description = models.TextField('Описание товара')
    price = models.IntegerField('Цена товара', default=0)
    
    def __str__(self):
        return self.product_title
    
    def get_absolute_url(self):
        return reverse("product:detail", kwargs={"product_slug": self.slug})
    