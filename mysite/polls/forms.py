from .models import Question, Choice
from django.forms import ModelForm, TextInput, DateTimeInput


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text']

    widgets = {
        'question_text': TextInput(attrs={
            'placeholder': 'Ваш вопрос',
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
