

# Create your views here.
from django.http import Http404
from .forms import CommentForm
from django.shortcuts import render
from .models import Blog
from .models import Comment


def get_home(request):
    return render(request , 'Home.html')

def get_blog(request):
    return render(request , 'Blog.html')

def get_contact(request):
    return render(request , 'Contact.html')


def get_blogs(request):
    ctx = {
        'blogs': Blog.objects.all().order_by('-created')
    }
    return render(request, 'blog-list.html', ctx)


def get_detail(request, blog_id):
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
            Comment.objects.create(**cleaned_data)
    ctx = {
        'blog': blog,
        'comments': blog.comment_set.all().order_by('-created'),
        'form': form
    }
    return render(request, 'blog-detail.html', ctx)