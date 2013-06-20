from django.conf.urls import patterns, url, include

from event import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        # /polls/5/
        #url(r'^(?P<event_id>\d+)/$', views.detail, name='index'),
        # /polls/5/results/
        #url(r'^(?P<event_id>\d+)/results/$', views.results, name='index'),
        # /polls/5/vote/
        #url(r'^(?P<event_id>\d+)/vote/$', views.vote, name='index'),
        )

