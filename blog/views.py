from django.views.generic import ListView, DetailView
from .models import Post, Category
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

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_category_post_count'] = Post.objects.filter(category=None).count()
        return context

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)

    return render(
        request,
        'blog/post_detail.html',
        {
            'post_detail': post,
        }
    )

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(cateogyr=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render(
        request,
        'blog/post_list.html',
        {
            'post_list': post_list,
            'categories': Category.objects.all(),
            'no_category_post_count': Post.objects.filter(category=None).count(),
            'category': category,
        }
    )




# Create your views here.
