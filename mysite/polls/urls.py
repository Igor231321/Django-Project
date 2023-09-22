"""Определяет схемы URL для polls."""
from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # Домашняя страница.
    path("", views.IndexView.as_view(), name='index'),
    # Страница с подробной информацией по отдельной теме.
    path('question/<int:id>/', views.question_detail, name='question_detail'),
    # Страница для Update
    path('question/<int:pk>/update/', views.QuestionUpdateView.as_view(), name='question_update'),
    # Страница для создания вопроса
    path('question/create/', views.question_create, name='new_question'),
    # Добавляет новую запись по конкретной теме.
    path('new_choice/<int:question_id>/', views.new_choice, name='new_choice'),
]
