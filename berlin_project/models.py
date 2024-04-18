from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=150)
    publisher = models.CharField(max_length=100)
    year = models.IntegerField()
    summary = models.ForeignKey('Review', on_delete=models.CASCADE, related_name="books", null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Review(models.Model):
    content = models.TextField(max_length=500, unique=True)
    book_title = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"You are reading the critique of the {self.book_title.title} - {self.content[:50]}"
