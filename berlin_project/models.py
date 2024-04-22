from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150, unique=True, blank=False)
    author = models.CharField(max_length=150, blank=False)
    publisher = models.CharField(max_length=100)
    year = models.IntegerField()
    description = models.TextField(blank=False)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Review(models.Model):
    content = models.TextField(max_length=500)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return f"Review of '{self.book.title}' - {self.content[:50]}"
