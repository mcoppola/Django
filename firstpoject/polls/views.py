from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
    return HttpResponse("Your looking at poll %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("Your looking at the results of poll %s" % poll_id)

def vote(request, poll_id):
    return HttpResponse("Your voting on poll %s." % poll_id)

