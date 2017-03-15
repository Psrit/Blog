# coding=utf-8
from django.contrib import admin

# Register your models here.
from article.models import Article, Category


# To display many-to-many relations using an inline, we can do so by defining
# an InlineModelAdmin object for the relationship:
class CategoriesInline(admin.TabularInline):
    # The through attribute is a reference to the model that manages the many-
    # to-many relation. This model is automatically created by Django when we
    # define a many-to-many field.
    model = Article.categories.through


class ArticleAdmin(admin.ModelAdmin):
    # fields = ['title', 'date_time', 'categories', 'content']
    fieldsets = [
        # The first element of each tuple in fieldsets is the title of
        # the fieldset
        (None, {'fields': ['title']}),
        ('Date information', {'fields': ['date_time'], 'classes': ['collapse']}),
        # ('Categories', {'fields': ['categories']}),
        ('Content', {'fields': ['content']})
    ]

    # Sometimes it’d be more helpful if we could display individual fields on
    # the change list page.
    # To do that, use the list_display admin option, which is a tuple of field
    # names to display, as columns, on the change list page for the object.
    # NOTE: The values of 'list_display' must not be a ManyToManyField.
    list_display = ('title', 'date_time',)

    # Adds a “Filter” sidebar that lets people filter the change list by the
    # date_time field and categories field.
    # The type of filter displayed depends on the type of field you’re filtering
    # on. Because date_time is a DateTimeField, Django knows to give appropriate
    # filter options: “Any date”, “Today”, “Past 7 days”, “This month”, “This year”.
    list_filter = ['date_time', 'categories']

    # Adds a search box at the top of the change list. When somebody enters
    # search terms, Django will search the field(s) in the 'search_fields' list.
    # For ForeignKey and ManyToManyField, combine the name of the field (here
    # 'categories', not 'Category') and related field name (to be searched) of
    # the foreign field (here 'name' of 'categories'):
    # 'categories__name'
    search_fields = ['title', 'content', 'categories__name']

    # To display the many-to-many relations using an inline (here
    # CategoriesInline), the ArticleAdmin must manually exclude the
    # 'categories' field (also, the 'fieldsets' or 'fields' mustn't contain
    # 'categories').
    # Django displays an admin widget for a many-to-many field on the model
    # that defines the relation (in this case, Article). If we want to use an
    # inline model to represent the many-to-many relationship, we must tell
    # Django’s admin to not display this widget - otherwise we will end up with
    # two widgets on our admin page for managing the relation.
    inlines = [CategoriesInline, ]
    exclude = ('categories',)


class CategoryAdmin(admin.ModelAdmin):
    inlines = [CategoriesInline, ]


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
