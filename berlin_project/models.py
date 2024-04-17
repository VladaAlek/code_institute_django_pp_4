from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    content = models.TextField(max_length=500, unique=True)

    def __str__(self):
        return self.content

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publisher = models.CharField(max_length=100)
    year = models.IntegerField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name="books", null=True, blank=True)

    def __str__(self):
        return self.title



