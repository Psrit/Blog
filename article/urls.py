# coding=utf-8
from django.conf.urls import url

from . import views

# set the application namespace so that Django knows which app view
# to create for a url when using the {% url %} template tag.
app_name = 'article'

urlpatterns = [
    # # ex: /polls/
    # url(r'^$', views.home, name='home'),
    # # ex: /polls/5/
    # # Using parentheses around a pattern “captures” the text matched
    # # by that pattern and sends it as an argument to the view function;
    # # ?P<question_id> defines the name that will be used to identify the
    # # matched pattern.
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^search/$', views.search_blog, name='search'),
]
