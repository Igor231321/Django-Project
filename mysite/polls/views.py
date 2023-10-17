from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from .forms import QuestionForm, ChoiceForm

from django.views import generic


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "questions_list"

    def get_queryset(self):
        """Возвращает список опубликованных вопросов."""
        return Question.published.all()[:3]


class QuestionUpdateView(generic.UpdateView):
    model = Question
    template_name = 'polls/new_question.html'

    fields = ['question_text']


def question_detail(request, question_slug):
    question = get_object_or_404(Question, slug=question_slug)
    return render(request, 'polls/detail.html', {"question": question})


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

