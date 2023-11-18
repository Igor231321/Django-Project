from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Product.Status.PUBLISHED)
    
    
class Product(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'
        
    product_title = models.CharField("Название товара", max_length=255)
    slug = models.SlugField("Короткая метка", max_length=255, blank=True, unique=True, db_index=True)
    description = models.TextField("Описание товара")
    ingredients = models.TextField("Ингридиенты")
    price = models.IntegerField("Цена товара", default=0)
    is_published = models.BooleanField("Текущее состояние", choices=Status.choices, default=Status.DRAFT)
    category = models.ForeignKey("Category", on_delete=models.PROTECT, related_name="posts", verbose_name="Категория")
    tags = models.ManyToManyField("TagProduct", blank=True, related_name="tags")
    
    objects = models.Manager() # Определяем старый менеджер, чтобы не пропал после определения нового
    published = PublishedManager() # Новый менеджер
      
    def get_absolute_url(self):
        return reverse("product:detail", args=[self.slug])
    
    def __str__(self):
        return self.product_title
    
    
class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)
    slug = models.SlugField("Короткая метка", max_length=255)

    def get_absolute_url(self):
        # return reverse("product:category", kwargs={"category_slug": self.slug})
        return reverse("product:category", args=[self.slug])
    
    def __str__(self):
        return self.name
    
    
class TagProduct(models.Model):
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    
    def __str__(self):
        return self.tag
        