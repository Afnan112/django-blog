from django.shortcuts import redirect, render
from blogs.models import Category, Blog
from core.models import About, SocialLink
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):
    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('-updated_at')

    posts = Blog.objects.filter(is_featured=False, status='Published')

    # Fetch about as
    try:
        about = About.objects.get()
    except:
        about = None

    context = {
        'featured_posts' : featured_posts,
        'posts' : posts,
        'about' : about,
    }
    return render(request, 'home.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid(): 
            # it will take out the username & password that user entered 
            # returns the dictionary of a validated input fields
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # this will take username & password and returns the user if that exists
            user = auth.authenticate(username=username, password=password)
            # exists
            if user is not None:
                auth.login(request, user)
            return redirect('home')
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

def logout(request):
    auth.logout(request)
    return redirect('home')