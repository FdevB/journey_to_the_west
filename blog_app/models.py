from django_ckeditor_5.fields import CKEditor5Field

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.
class CategoryModel(models.Model):
    """
    Create a category model for set the ctaegories for posts in our Blog_app

    Field:
        1. name: name of category
        2. slug: a link derived from the name (non-editable)
    """

    name = models.CharField(max_length=50)

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class TagModel(models.Model):
    """
    Create a tag model for set the tags for posts in our Blog_app

    Field:
        1. name: name of tag
        2. slug: a link derived from the name (non-editable)
    """

    name = models.CharField(max_length=50)

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Tag'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class PostModel(models.Model):
    """
    Create a post model for posts in our Blog_app
    
    Field:
        1. title: title of post
        2. description: description of post
            2.1. I used 'CKEditor' to increase the flexibility and capabilities of the structure. but if you dont want it can use simple way
        3. banner: banner of post
        4. author: author of post 1:n relation
        5. categories: categories of post
        6. tags: tags of post m:n relation
        7. status: status of post (pub or draft)
        8. views: count of views of post
        9. created_at: date of create post
        10. updated_at: date of update post
        11. published_at: datetime of pubish post
        12. slug: a link derived from the title (non-editable)
    """

    title = models.CharField(max_length=150)
    description = CKEditor5Field(config_name='extends')  # You can USE models.TextField()

    banner = models.ImageField(upload_to='blog/post_banner/')

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    categories = models.ManyToManyField(CategoryModel, related_name='post')
    tags = models.ManyToManyField(TagModel, related_name='post')

    status = models.BooleanField(default=False)
    views = models.BigIntegerField(default=0)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    published_at = models.DateTimeField()

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Post'
        ordering = ['-updated_at']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
