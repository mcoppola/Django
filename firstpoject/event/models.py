from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=200)
    event_date = models.DateTimeField('event date')
    pub_date = models.DateTimeField('date published')

    def __unicode__(self):
        return self.title

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'