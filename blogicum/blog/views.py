from django.shortcuts import render
from django.http import Http404


def index(request):
    template = 'blog/index.html'
    context = {'posts': list(posts_dict.values())[::-1]}
    return render(request, template, context)


def category_posts(request, category_slug):
    template = 'blog/category.html'
    context = {'category': category_slug}
    return render(request, template, context)


def post_detail(request, id):
    post = posts_dict.get(id)
    if not post:
        raise Http404("Пост не найден")
    template = 'blog/detail.html'
    context = {'post': post}
    return render(request, template, context)
