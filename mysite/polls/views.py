from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from .forms import QuestionForm, ChoiceForm


def index_page(request):
    """Домашняя страница приложения Polls."""
    return render(request, 'polls/index.html')


def questions_page(request):
    """Выводит список вопросов."""
    questions_list = Question.objects.order_by("-pub_date")
    context = {'questions': questions_list}
    return render(request, 'polls/questions.html', context)


def question_detail(request, question_id):
    """Выводит один вопрос."""
    question = get_object_or_404(Question, pk=question_id)
    choice = get_object_or_404(Choice, pk=question_id)
    context = {'question': question,
               'choice': choice}
    return render(request, 'polls/detail.html', context)


def question_create(request):
    """Создание вопроса."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = QuestionForm()
    else:
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('polls:index')

    # Вывести пустую или недействительную форму.
    context = {'form': form}
    return render(request, 'polls/new_question.html', context)


def new_choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method != 'POST':
        # Данные не отправились; создается пустая форма.
        form = ChoiceForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = ChoiceForm(request.POST)
        if form.is_valid():
            new_choice = form.save(commit=False)
            new_choice.question = question
            new_choice.save()
            return redirect('polls:questions')

    # Вывести пустую или недействительную форму.
    context = {'question': question, 'form': form}
    return render(request, 'polls/new_choice.html', context)
