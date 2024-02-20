from django.shortcuts import render
from datetime import date

from .models import Author,Post,Category
def post_list(request):
    category_name = request.GET.get('category_name')
    posts = Post.objects.all()
    
    categories = Category.objects.all()

    if category_name is not None:
        posts = posts.filter(category__name = category_name)
    

    return render(request, 'app/posts.html', context={'posts': posts, 'categories': categories})


def post_detail(request, pk):

    post = Post.objects.filter(pk = pk).first()

    return render(request, 'app/post.html', context={'post': post})


def author_detail(request, pk):

    author = Author.objects.get(pk = pk)

    return render(request, 'app/author.html', context={'author': author})


