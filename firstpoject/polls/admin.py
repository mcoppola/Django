from django.contrib import admin 
from polls.models import Poll
from polls.models import Choice


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': ['question']}),
            ('Date information', {'fields': ['pub_date']}),
        ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    list_display = ('question', 'pub_date', 'was_published_recently')
    
admin.site.register(Poll, PollAdmin)

