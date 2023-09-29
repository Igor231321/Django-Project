from django.db import models
from django.urls import reverse


class Question(models.Model):
    question_text = models.CharField('Название вопроса', max_length=50)
    slug = models.SlugField(max_length=50, unique=True, db_index=True, default='')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.question_text

    class Meta:
        ordering = ['-pub_date']
        indexes = [
            models.Index(fields=['-pub_date'])
        ]

    def get_absolute_url(self):
        return reverse('question_detail', kwargs={'question_slug': self.slug})


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Ваш ответ:', max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
