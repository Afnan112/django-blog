from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from .models import Blog, Category


# Create your views here.
def posts_by_category(request, category_id):
    # Fetch the posts that belongs to the category with the id category_id
    posts = Blog.objects.filter(category=category_id, status='Published')
    # Category isn't exist
    # Use try/except when we want to do some custom action if the category does not exist
    # try:
    #     # category_id => URL
    #     # ID => column in DB 
    #     category_name = Category.objects.get(id=category_id) 
    #     #print(category_name)
    # # Will go here
    # except:
    #     # redirect the user to home page
    #     return redirect('home')
    
    # Use get_object_or_404 when you want to show a 404 error page if the category does not exist
    category_name = get_object_or_404(Category, id=category_id)

    # To send data from VIEW to TEMPLATE
    context = {
        'posts' : posts,
        'category' : category_name
    }
    return render(render, 'posts_by_category.html', context)