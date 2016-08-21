

# Create your views here.
from django.http import Http404
from .forms import *
from django.shortcuts import render
from .models import *
import math


def get_home(request):
    request.session['max_blogs'] = Blog.objects.all().count()
    request.session['max_books'] = Book.objects.all().count()
    return render(request , 'Home.html')

def get_book(request , pa_id=1):
    pa_id = int(pa_id)
    choose = pa_id
    min_id = (pa_id - 1) * 20
    max_id = pa_id * 20

    max_books = request.session.get('max_books', default='0')
    max_books = range(1, math.ceil(max_books / 20.0) + 1)

    ctx = {
        'books': Book.objects.all().order_by('-created')[min_id:max_id],
        'max_books': max_books,
        'choose': choose,
    }

    return render(request , 'Book.html' , ctx)

def get_blog(request , pa_id=1):
    pa_id = int(pa_id)
    choose = pa_id
    min_id  =  (pa_id - 1 ) * 20
    max_id = pa_id * 20

    max_blogs = request.session.get('max_blogs', default='0')
    max_blogs = range(1 ,math.ceil(max_blogs / 20.0) + 1)


    ctx = {
        'blogs': Blog.objects.all().order_by('-created')[min_id:max_id],
        'max_blogs' : max_blogs,
        'choose' : choose,
    }
    return render(request , 'Blog.html' , ctx)

def get_contact(request):
    return render(request , 'Contact.html')




# def get_blogs(request):
#     ctx = {
#         'blogs': Blog.objects.all().order_by('-created')
#     }
#     return render(request, 'blog-list.html', ctx)

def test(request):

    return render(request, 'test.html')


def blog_get_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except Blog.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Blog_Comment.objects.create(**cleaned_data)
    ctx = {
        'blog': blog,
        'comments': blog.blog_comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'detail_blog.html', ctx)


def book_get_detail(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404

    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            cleaned_data['book'] = book
            Book_Comment.objects.create(**cleaned_data)


    ctx = {
        'book': book,
        'comments': book.book_comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'detail_book.html', ctx)