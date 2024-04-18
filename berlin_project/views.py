from django.shortcuts import render
#from django.http import HttpResponse
from django.views import generic
from .models import Book

# Create your views here.
#def index(request):
    #return HttpResponse("Hello, you are in the Berlin Project")

class BookList(generic.ListView):
    #model = Book
    queryset = Book.objects.all()
    template_name = "book_list.html"

