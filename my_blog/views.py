from __future__ import print_function

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from article.models import Article, Category

num_posts_per_page = 3


def home(request):
    # Deprecated:
    # post_list = Article.objects.all()
    # return render(request, 'home.html', {'post_list': post_list})

    posts = Article.objects.all()
    # Show 'num_posts_per_page' posts (blogs) per page
    paginator = Paginator(posts, num_posts_per_page)

    # The number of the page to be visited, starting from 1:
    page_number = request.GET.get('page')

    try:
        post_list = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer, deliver first page.
        post_list = paginator.page(1)
    except EmptyPage:
        # If page_number is out of range (e.g. 9999), deliver last page of
        # results.
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})


def archives(request):
    try:
        category_list = Category.objects.all()
    except Category.DoesNotExist:
        raise Http404

    try:
        having_articles = (Article.objects.all().count() > 0)
    except Article.DoesNotExist:
        raise Http404

    return render(request, 'archives.html',
                  {'category_list': category_list,
                   'display': "none",
                   'having_articles': having_articles
                   })


def search_tag(request, name):
    try:
        category_list = Category.objects.filter(name__exact=str(name))
    except Category.DoesNotExist:
        raise Http404
    return render(request, 'archives.html',
                  {'category_list': category_list,
                   'display': "block",
                   'having_articles': True
                   })


def about_me(request):
    return render(request, "aboutme.html")
