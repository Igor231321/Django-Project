from django.db import models
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Question.Status.PUBLISHED)


class Question(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    question_text = models.CharField('Название вопроса', max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, default='')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(choices=Status.choices, default=Status.PUBLISHED)

    objects = models.Manager()
    published = PublishedManager()

    class Meta:
        ordering = ['-pub_date']
        indexes = [
            models.Index(fields=['-pub_date'])
        ]

    def get_absolute_url(self):
        return reverse('polls:question_detail', args=[self.slug])

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Ваш ответ:', max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
