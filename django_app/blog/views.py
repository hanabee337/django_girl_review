# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone

from .models import Post


def post_list(request):
    # return HttpResponse('post_list view')

    posts = Post.objects.filter(
        published_date__lte=timezone.now())

    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)
