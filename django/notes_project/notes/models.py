from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
	user = models.ForeignKey(User)
	date = models.DateTimeField('date published')
	text = models.CharField(max_length=300)

	def __unicode__(self):
		return self.text
