from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.core.cache import cache

from blog_app.models import PostModel

@receiver(pre_save, sender=PostModel)
def store_old_slug(sender, instance, **kwargs):
    if instance.pk is None:
        instance._old_slug = None
        return
    
    try:
        old_post = PostModel.objects.get(pk=instance.pk)
        instance._old_slug = old_post.slug
    except PostModel.DoesNotExist:
        instance._old_slug = None

@receiver(post_save, sender=PostModel)
def clear_data_cache(sender, instance, created, **kwargs):
    if created:
        return

    old_slug = getattr(instance, '_old_slug', None)

    if old_slug:
        cache_key = f"post_detail:{old_slug}"
        cache.delete_many([cache_key, 'published_posts'])

    delattr(instance, '_old_slug')
