# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .forms import PostForm
from .models import Post


def post_list(request):
    # return HttpResponse('post_list view')

    posts = Post.objects.filter(
        published_date__lte=timezone.now())

    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)


def post_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)

    context = {
        'post_detail': post,
    }

    return render(request, 'blog/post_detail.html', context)


def post_add(request):
    # return HttpResponse('post_add view')

    if request.method == 'POST':
        print(request.POST)
        return HttpResponse('post_add view')
    else:
        forms = PostForm()
        context = {
            'forms': forms,
        }
        return render(request, 'blog/post_add.html', context)
