# coding=utf-8
from __future__ import unicode_literals

from django.db import models

# When making model changes, do the follows step-by-step:
# 1. Change your models (in models.py).
# 2. Run python manage.py makemigrations to create migrations for those changes
# 3. Run python manage.py migrate to apply those changes to the database.

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Article(models.Model):
    title = models.CharField(max_length=100)

    # To get categories of some article a, use: a.categories.all()/get(pk=1)/add(c)
    # To get articles which are of some category c, use: py.article_set.all()/get(pk=1)
    categories = models.ManyToManyField(Category, verbose_name='categories')

    # auto_now_add=True makes date_time a non-editable field
    date_time = models.DateTimeField('date published')  # (auto_now_add=True)

    content = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        path = reverse('blog', kwargs={'id': self.id})
        return "http://127.0.0.1:8000%s" % path

    def __str__(self):
        return self.title

    class Meta:
        """
        Give your model metadata by using an inner class Meta.

        Model metadata is “anything that’s not a field”, such as ordering
        options (ordering), database table name (db_table), or human-readable
        singular and plural names (verbose_name and verbose_name_plural).
        None are required, and adding class Meta to a model is completely
        optional.

        """
        ordering = ['-date_time']
