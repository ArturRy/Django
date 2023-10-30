from books.models import Book
from django.shortcuts import render

def show_book():

    book = Book.objects.filter(name='Ведьмак')

    print(book)