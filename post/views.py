from django.shortcuts import render
from . models import Post



def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/post_details.html', {
        'post': post
    })
