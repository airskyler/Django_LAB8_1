from django.db import models
from django.utils import timezone


class Post(models.Model):

	# ForeignKey to user model
    author = models.ForeignKey('auth.User')
	
	# setting the max length of the title character to 200
    title = models.CharField(max_length=200)
	
	# Use TextField to hold large text string
    text = models.TextField()
	
	# getting a current date and time in specific timezone
    created_date = models.DateTimeField(
            default=timezone.now)
			
	# getting a published date and time
    published_date = models.DateTimeField(
            blank=True, null=True)

			
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

