from django.core.paginator import Paginator
from django.shortcuts import render

from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, template, context)


def show_book(request):
    template = 'books/book_show.html'
    books = Book.objects.all()
    sort_books = []
    for c in list(sorted(books, key=lambda x: x.pub_date)):
        sort_books.append(c)
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(sort_books, 1)
    page = paginator.get_page(page_number)
    book = Book.objects.filter(name='Ведьмак')
    context = {
        'book': book
    }
    return render(request, template, context)

