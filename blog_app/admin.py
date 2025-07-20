from django.contrib import admin

from blog_app import models

# Register your models here.
@admin.register(models.CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    """
    create model controler in admin page for categories

    Field:
        1. readonly_fields (slug): in admin page slug just readable 
    """
    
    readonly_fields = ['slug']

@admin.register(models.TagModel)
class TagAdmin(admin.ModelAdmin):
    """
    create model controler in admin page for tags

    Field:
        1. readonly_fields (slug): in admin page slug just readable 
    """

    readonly_fields = ['slug']

@admin.register(models.PostModel)
class PostAdmin(admin.ModelAdmin):
    """
    create model controler in admin page for posts

    Field:
        1. date_hierarchy (published_at): enables date-based navigation
        2. list_display: columns to show
        3. list_filter: sidebar filters
        4. search_fields: searchable fields
        5. readonly_fields (slug): it is read-only 
    """

    date_hierarchy = 'published_at'
    list_display = ['title', 'author', 'status', 'updated_at', 'published_at', 'views']
    list_filter = ['author', 'categories', 'tags', 'status', 'updated_at']
    search_fields = ['title']
    readonly_fields = ['slug']
