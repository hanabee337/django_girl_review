# Create your views here.
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import PostForm
from .models import Post


def post_list(request):
    # return HttpResponse('post_list view')

    # posts = Post.objects.filter(
    #     published_date__lte=timezone.now())
    posts = Post.objects.all()

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
        # return HttpResponse('post_add view')

        data = request.POST
        forms = PostForm(data=data)
        # return redirect('post_list')
        author = User.objects.get(id=1)

        if forms.is_valid():
            print('forms.cleaned_data: {}'.format(forms.cleaned_data))
            title = forms.cleaned_data['title']
            text = forms.cleaned_data['text']

            post = Post.objects.create(
                title=title,
                text=text,
                author=author
            )
            # return redirect('post_list')
            return redirect('post_detail', post_id=post.id)
        else:
            return HttpResponse('Invalid Form')
    else:
        forms = PostForm()
        context = {
            'forms': forms,
        }
        return render(request, 'blog/post_add.html', context)


def post_delete(request, post_id):
    # return HttpResponse('post_delete view')
    if request.method == 'POST':
        print(request.POST)

        post = Post.objects.get(id=post_id)
        post.delete()

        return redirect('post_list')
    else:
        forms = PostForm()
        context = {
            'forms': forms,
        }
        return render(request, 'blog/post_delete.html', context)
