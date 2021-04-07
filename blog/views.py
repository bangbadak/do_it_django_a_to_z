from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render

def PostList(ListView):
    model = Post
    ordering = '-pk'

def PostDetail(DetailView):
    model = Post
#   template_name = 'blog/post_list.html'


def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': posts,
        }
    )

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/post_detail.html',
        {
            'post_detail': post,
        }
    )

# Create your views here.
