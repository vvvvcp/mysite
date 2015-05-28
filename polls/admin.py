from django.contrib import admin
from polls.models import Question
from polls.models import Choice
from polls.models import Vote
from polls.models import Member


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Choice)
admin.site.register(Question, QuestionAdmin)

admin.site.register(Vote)
admin.site.register(Member)
