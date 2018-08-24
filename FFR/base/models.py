from django.db import models

# Create your models here.
class story(models.Model):
	title = models.TextField()
	author = models.CharField(max_length=256)
	content = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now_add=True)
	upvotes = models.IntegerField(default=0)
	downvotes = models.IntegerField(default=0)
	