from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):  # or admin.StackedInline
    model = Choice
    extra = 3  # Number of empty choices to show in the admin form for Question

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Register the models with the admin site
admin.site.register(Question, QuestionAdmin)
