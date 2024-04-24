from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Book

# Create your views here.
def index(request):
    return render(request, 'index.html')

#def Main_page(request):
    #return render(request, 'berlin_project/index.html')


class BookList(generic.ListView):
    #model = Book
    queryset = Book.objects.all()
    template_name = "book_list.html"


#class Main_page(generic.ListView):
    #model = Book
    #queryset = Book.objects.all()
    #template_name = "main_page.html"

