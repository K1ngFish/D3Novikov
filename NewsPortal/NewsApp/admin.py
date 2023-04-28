from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class PostCategoryInline(admin.TabularInline):
     model = PostCategory
     extra = 1


class PostAdmin(TranslationAdmin):
     list_display = ('title', 'author', 'dateCreation', 'category_type', 'rating')
     list_filter = ('author', 'dateCreation')
     search_fields = ('title', 'author')
     model = Post


class CategoryAdmin(TranslationAdmin):
     model = Category
     list_display = ('name',)
     inlines = [PostCategoryInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)

