# from re import template
from django.shortcuts import render, get_object_or_404
# Create your views here.
# from django.http import HttpResponse
from .models import Post, Group
AMOUNT_POSTS_ON_PAGE = 10


def index(request):
    # Одна строка вместо тысячи слов на SQL:
    # в переменную posts будет сохранена выборка из 10 объектов модели Post,
    # отсортированных по полю pub_date по убыванию
    # (от больших значений к меньшим)
    posts = Post.objects.all()[:AMOUNT_POSTS_ON_PAGE]
    # В словаре context отправляем информацию в шаблон
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts_of_group.all()[:AMOUNT_POSTS_ON_PAGE]
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, 'posts/group_list.html', context)
