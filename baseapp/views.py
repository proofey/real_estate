from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from post.models import Post
from . forms import LoginForm, SearchForm
from django.contrib.auth import authenticate, login, logout
from . search import search


def home_page(request):
    search_form = SearchForm()
    posts = Post.objects.all()
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'baseapp/home_page.html', {
        'page_obj': page_obj,
        'search_form': search_form
    })


def login_request(request):
    if request.method == "POST":
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home-page')
    else:
        form = LoginForm()
    return render(request, 'baseapp/login.html', {
        'form': form
    })

def logout_request(request):
    logout(request)
    return redirect('home-page')


def search_request(request):
    search_form = SearchForm(data=request.GET)
    posts = search(request)
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'baseapp/home_page.html', {
        'page_obj': page_obj,
        'search_form': search_form
    })