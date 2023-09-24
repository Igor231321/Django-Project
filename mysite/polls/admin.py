from django.contrib import admin
from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Question information", {'fields': ['question_text']})
    ]
    inlines = [ChoiceInline]

    list_display = ['question_text', 'pub_date']
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
