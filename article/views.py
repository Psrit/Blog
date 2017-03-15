from django.http import Http404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

# Create your views here.
from article.models import Article


def detail(request, id):
    post = get_object_or_404(Article, pk=id)
    return render(request, 'post.html', {'post': post})


def search_blog(request):
    """
    Only supports to search (by words in the titles) from the search form.
    Visiting "/blog/search/some_keywords" will be redirected to the home page.

    """
    if "search" in request.GET:
        search_target = request.GET["search"]
        if not search_target:
            return render(request, "home.html")
        else:
            article_set = Article.objects.filter(title__icontains=search_target)
            if (article_set.count() == 0):
                return render(request, 'search.html',
                              {'article_set': article_set,
                               'having_articles': False
                               })
            else:
                return render(request, 'search.html',
                              {'article_set': article_set,
                               'having_articles': True
                               })

    return HttpResponseRedirect("/")
