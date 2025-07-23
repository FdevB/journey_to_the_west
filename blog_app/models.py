from django_ckeditor_5.fields import CKEditor5Field

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone

# Create your models here.
class CategoryModel(models.Model):
    """
    Model definition for CategoryModel.

    This class defines the CategoryModel database schema and its related behaviors.

    Attributes:
        name (CharField): Name of category.
        slug (SlugField): A link derived from the name (non-editable).
    """

    name = models.CharField(max_length=50)

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """
        Overrides the default save method to automatically set the slug field.
        """
        
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class TagModel(models.Model):
    """
    Model definition for TagModel.

    This class defines the TagModel database schema and its related behaviors.

    Attributes:
        name (CharField): Name of category.
        slug (SlugField): A link derived from the name (non-editable).
    """

    name = models.CharField(max_length=50)

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Tag'

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        """
        Overrides the default save method to automatically set the slug field.
        """

        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class PostModel(models.Model):
    """
    Model definition for PostModel.

    This class defines the PostModel database schema and its related behaviors.
    This model uses CKEditor for the description field to provide rich text editing capabilities. If not required, it can be replaced with a standard TextField.

    Attributes:
        title (CharField): Title of the post.
        description (CKEditor5Field): Description of the post with rich text support.
        banner (ImageField): Banner image of the post.
        author (ForeignKey to User): Author of the post.
        categories (ManyToManyField to CategoryModel): Categories assigned to the post.
        tags (ManyToManyField to TagModel): Tags assigned to the post.
        status (BooleanField): Status of the post (published or draft).
        views (BigIntegerField): Number of views for the post.
        created_at (DateField): Date when the post was created.
        updated_at (DateField): Date when the post was last updated.
        published_at (DateTimeField): Date and time when the post was published.
        slug (SlugField): Slug derived from the title (non-editable).
    """

    title = models.CharField(max_length=150)
    description = CKEditor5Field(config_name='extends')  # You can USE models.TextField()

    banner = models.ImageField(upload_to='blog/post_banner/')

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    categories = models.ManyToManyField(CategoryModel, related_name='post')
    tags = models.ManyToManyField(TagModel, related_name='post')

    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published')
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    views = models.BigIntegerField(default=0)

    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name = 'Post'
        ordering = ['-updated_at']

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        """
        Overrides the default save method to automatically set the slug field.
        """ 

        self.slug = slugify(self.title)

        if (self.status == 'published') and (self.published_at is None):
            self.published_at = timezone.now()

        elif (self.published_at is not None) and (timezone.now() >= self.published_at):
            self.status = 'published'

        else:
            self.status = 'draft'

        super().save(*args, **kwargs)
