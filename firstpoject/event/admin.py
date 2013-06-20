from django.contrib import admin 
from event.models import Event


class EventAdmin(admin.ModelAdmin):
    fieldsets = [
            (None,               {'fields': ['title']}),
            ('Date information', {'fields': ['event_date']}),
            ('Post date', {'fields': ['pub_date']}),
        ]
    #inlines = [ChoiceInline]
    list_filter = ['event_date']
    date_hierarchy = 'event_date'
    list_display = ('title', 'pub_date', 'event_date')
    
admin.site.register(Event, EventAdmin)

