from django.http import HttpResponse


# Create your views here.
def post_list(request):
    return HttpResponse('post_list view')
