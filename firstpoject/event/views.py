from django.http import HttpResponse
from django.template import Context, loader

from event.models import Event

def index(request):
	e = Event.objects.all()
	template = loader.get_template('event/index.html')
	context = Context({'latest_event_list': e,})
	return HttpResponse(template.render(context))

    