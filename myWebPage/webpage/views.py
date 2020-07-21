from django.shortcuts import render
from .models import Post

# Create your views here.
def my_list(request):
    post = Post.objects.all()
    context = {
        'my_list': post

    }
    return render(request, 'webpage/list.html', context)

def list_detail(request, id):
    each_post = Post.objects.get(id=id)
    context = {
        'list_detail': each_post
    }
    return render(request, 'webpage/list_detail.html', context)