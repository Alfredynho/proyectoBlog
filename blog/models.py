from django.db import models

from django.utils.translation import ugettext as _
from django.utils import timezone

class Post(models.Model):
	autor = models.ForeignKey(
		'auth.User'
	)

	title = models.CharField(
		max_length=200
	)

	text = models.TextField(
		verbose_name= _('text')
	)

	creted_date = models.DateTimeField(
		default=timezone.now
	)

	publish_date = models.DateTimeField(
		blank=True, 
		null=True
		)

	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title
