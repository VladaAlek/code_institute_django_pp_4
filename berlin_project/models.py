from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):
	title = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="book_reviews")
	author = models.CharField(max_length=150)
	publisher = models.CharField(max_length=100)
	year = models.IntegerField()

	def __str__(self):
    	return self.title.content

