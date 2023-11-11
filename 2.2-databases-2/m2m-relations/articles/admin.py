from django.contrib import admin

from .models import Article, Tag, ArticleTag


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'published_at',]
    inlines = [ArticleTagInline, ]

    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['subject']

