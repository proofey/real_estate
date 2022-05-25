from django.shortcuts import render
from django.core.paginator import Paginator
from post.models import Post


def home_page(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'baseapp/home_page.html', {
        'page_obj': page_obj
    })