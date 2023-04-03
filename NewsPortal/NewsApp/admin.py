from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'dateCreation', 'category_type', 'rating')
    list_filter = ('author', 'dateCreation')
    search_fields = ('title', 'author')


admin.site.register(Category)
admin.site.register(Post, PostAdmin)

