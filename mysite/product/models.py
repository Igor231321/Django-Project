from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Product.Status.PUBLISHED)
    
    
class Product(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'
        
    product_title = models.CharField('Название товара', max_length=255)
    slug = models.SlugField("Короткая метка", max_length=255, blank=True, unique=True, db_index=True)
    description = models.TextField('Описание товара')
    price = models.IntegerField('Цена товара', default=0)
    is_published = models.BooleanField("Текущее состояние",choices=Status.choices, default=Status.DRAFT)
    
    objects = models.Manager() # Определяем старый менеджер, чтобы не пропал после определения нового
    published = PublishedManager() # Новый менеджер
      
    def get_absolute_url(self):
        return reverse("product:detail", kwargs={"product_slug": self.slug})
    
    def __str__(self):
        return self.product_title
    