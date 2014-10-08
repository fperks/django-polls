from django.contrib import admin
from polls.models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': ['question_text']
        }),
        ('Date Information', {
            'fields' : ['publish_date'],
            'classes': ['collapse']
        })
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'publish_date', 'was_published_recently')


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)



