# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render


def post_list(request):
    # return HttpResponse('post_list view')
    context = {

    }
    return render(request, 'blog/post_list.html', context)
