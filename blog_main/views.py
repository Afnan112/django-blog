from django.shortcuts import render
from blogs.models import Category, Blog


def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')
    #print(featured_posts)

    posts = Blog.objects.filter(is_featured=False, status='Published')
    #print(posts)

    context = {
        'featured_posts' : featured_posts,
        'posts' : posts
    }
    return render(request, 'home.html', context)