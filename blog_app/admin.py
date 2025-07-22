from django.contrib import admin

from blog_app import models

# Register your models here.
@admin.register(models.CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin configuration for the CategoryModel.

    This class registers CategoryModel in the Django admin interface with all its features.

    Attributes:
        readonly_fields (list[str]): A list of field names to set as read-only.
    """
    
    readonly_fields = ['slug']

@admin.register(models.TagModel)
class TagAdmin(admin.ModelAdmin):
    """
    Admin configuration for the TagModel.

    This class registers TagModel in the Django admin interface with all its features.

    Attributes:
        readonly_fields (list[str]): A list of field names to set as read-only.
    """

    readonly_fields = ['slug']

@admin.register(models.PostModel)
class PostAdmin(admin.ModelAdmin):
    """
    Admin configuration for the PostModel.

    This class registers PostModel in the Django admin interface with all its features.

    Attributes:
        date_hierarchy (str): Enables date-based navigation by the specified date field.
        list_display (list[str]): Fields to display as columns in the list view.
        list_filter (list[str]): Fields to filter by in the sidebar.
        search_fields (list[str]): Fields that are searchable in the admin.
        readonly_fields (list[str]): Fields set as read-only in the admin form.
    """

    date_hierarchy = 'published_at'
    list_display = ['title', 'author', 'status', 'updated_at', 'published_at', 'views']
    list_filter = ['author', 'categories', 'tags', 'status', 'updated_at']
    search_fields = ['title']
    readonly_fields = ['slug']
