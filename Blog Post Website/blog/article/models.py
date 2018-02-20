from django.db import models

from django.utils import timezone

# Create your models here.

class articleContent(models.Model):
	articleTitle = models.CharField( max_length = 20)
	articleBody = models.TextField()
	date_added = models.DateTimeField( default = timezone.now)

	def __str__(self):
		return 'Title : {}, ID : {}'.format( self.articleTitle, self.id)