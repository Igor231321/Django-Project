from .models import Question, Choice
from django.forms import ModelForm, TextInput, DateTimeInput


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'pub_date']

    widgets = {
        'question_text': TextInput(attrs={
            'placeholder': 'Ваш вопрос',
            'class': 'form-control'
        }),
        'pub_date': DateTimeInput(attrs={
            'class': 'form-control'
        })
    }


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ['choice_text']

        widgets = {
            'choice_text': TextInput(attrs={
                'placeholder': 'Ваш ответ'
        })
        }
