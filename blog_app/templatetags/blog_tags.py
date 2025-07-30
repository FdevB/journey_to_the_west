from django import template
from django.contrib.auth.models import User

from blog_app.models import PostModel, CategoryModel, TagModel

import random


register = template.Library()

@register.filter(name='get_random')
def get_random_objects(sequence, count=1):
    """
    Return a list of `count` random objects selected from the given sequence.

    Arguments:
        sequence (list): A sequence of any objects.
        count (int): Number of random items to return.

    Returns:
        random_objects (list): List of random object from sequence.
    """

    if not sequence:
        sequence = []

    sequence = list(sequence)
    count = min(count, len(sequence))
    random_objects = random.sample(sequence, k=count)

    return list(random_objects)


@register.simple_tag(name='get_same')
def get_same_objects(sequence, related_name, kind='c'):
    """
    Return a list of objects that share at least one category with the items in the sequence,
    but are not themselves in the sequence.

    Arguments:
        kind (str): Select subscription type.
        sequence (list): A sequence of any objects.
        related_name (str): A related_name for reverse relation.

    Variable:
        types (dict): All selected modes for the subscription type.

    Returns:
        same_object (list): List of objects that are similar in category from sequence.
    """

    types = {
        't': 'tags',
        'u': 'author',
        'c': 'categories',
    }

    same_object = set()
    if (kind == 't') or (kind == 'c'):
        for item in sequence:
            for common_ground in getattr(item,  types[kind]).all():
                same_object.update(getattr(common_ground, related_name).all())

    else:
        for item in sequence:
            user = item.author
            same_object.update(getattr(user, related_name).all())

    same_object = list(same_object - set(sequence))

    return same_object


@register.filter(name='sort_by')
def sort_objects_by(sequence, field_with_limit):
    """
    Return a sorted list of objects in a sequence with given field.

    Arguments:
        sequence (Queryset): A sequence of any objects.
        field_with_limit (str): Field name to sort by, optionally followed by a count (e.g. "-created 10").

    Returns:
        sorted_objects (Queryset): Queryset of objects sorted by filter_field and len args[0].
    """

    parts = field_with_limit.split()
    field = parts[0] if parts else None
    count = int(parts[1]) if len(parts) == 2 and parts[1].isdigit() else None

    if not field:
        return sequence

    sorted_objects = (sequence.order_by(field)[:count]) if count else (sequence.order_by(field))


    return sorted_objects


@register.inclusion_tag('blog_app/blog_sidebar.html', name='side_bar')
def include_blog_sidebar():
    """
    Return a dict to blog_app/blog_sidebar.html as context.

    Variable:
        posts (Queryset): A sequence of all Post objects.
        users (Queryset): A sequence of all User objects.
        Tags (Queryset): A sequence of all Tag objects.
        raw_categories (Queryset): A sequence of all Categories objects.
        categories (dict): A dict to give name as key and count of post as value.

    Returns:
        data (dict): return a context as data name.
    """

    posts = PostModel.objects.filter(status='published')
    users = User.objects.all()
    raw_categories = CategoryModel.objects.all()
    tags = TagModel.objects.all()

    categories = {}
    for category in raw_categories:
        name = category.name
        slug = category.slug
        count = posts.filter(categories__name=name).count()

        categories[name] = [slug, count]

    data = {
        'posts': posts,
        'users': users,
        'tags': tags,
        'categories': categories,
    }

    return data
