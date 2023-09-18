"""Определяет схемы URL для polls."""
from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
    # Домашняя страница.
    path("", views.index_page, name='index'),
    # Страница с товаром.
    path('questions/', views.questions_page, name='questions'),
    # Страница с подробной информацией по отдельной теме.
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    # Страница для создания вопроса
    path('question/create/', views.question_create, name='new_question'),
    # Добавляет новую запись по конкретной теме.
    path('new_choice/<int:question_id>/', views.new_choice, name='new_choice'),
]


