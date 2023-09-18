from django.db import models


class Question(models.Model):
    question_text = models.CharField('Название вопроса', max_length=50)
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField('Ваш ответ:', max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
