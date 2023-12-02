from django.contrib import admin
from .models import Choice, Question

# Register your models here.

# allow poll to be modified by user and create more fields


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# more fields to fill in to make it easier
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    # allow filters and search fields
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


admin.site.register(Question, QuestionAdmin)
