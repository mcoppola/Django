from django.db import models

# Create your models here.

class Hypo(models.Model):
	question = models.CharField(max_length=200)
	pub_date = models.DateTimeField('date_published')
	votes = models.IntegerField(default=0)

	def __unicode__(self):
		return self.question

class Reply(models.Model):
	hypo = models.ForeignKey(Hypo)
	reply_text = models.CharField(max_length=200)

	def __unicode__(self):
		return self.reply_text