from django.shortcuts import redirect, render
from django.urls import reverse
from . models import Post
from . forms import PostForm
from django.contrib.auth.decorators import login_required



def post_details(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post/post_details.html', {
        'post': post
    })

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-page')
    else:
        form = PostForm()
    return render(request, 'post/new_post.html', {
        'form': form
    })

@login_required
def delete_post(request, id: int):
    post = Post.objects.get(id=id)
    if request.user.is_authenticated:
        post.delete()
        return redirect('home-page')

@login_required
def update_post(request, id: int):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect(reverse('post-details', args=(post.id,)))
    else:
        form = PostForm(instance=post)
    return render(request, 'post/update_post.html', {
        'form': form,
        'post': post
    })