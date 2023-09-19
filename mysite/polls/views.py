from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice
from .forms import QuestionForm, ChoiceForm
from django.views import generic


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questions_list"

    def get_queryset(self):
        """Возвращает список опубликованных вопросов."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    """Выводит один вопрос."""
    model = Question
    template_name = "polls/detail.html"


class UpdateView(generic.UpdateView):
    model = Question
    template_name = "polls/new_question.html"

    form_class = QuestionForm


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
