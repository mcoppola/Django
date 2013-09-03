from django.contrib import admin
from hypo.models import Hypo, Reply

class HypoAdmin(admin.ModelAdmin):
	fields = ['pub_date', 'question', 'votes']

admin.site.register(Hypo, HypoAdmin)
admin.site.register(Reply)
