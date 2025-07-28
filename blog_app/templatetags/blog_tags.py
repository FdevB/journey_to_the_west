from django import template
from django.template.defaultfilters import stringfilter

import random

from blog_app.models import CategoryModel

register = template.Library()

@register.filter(name='get_random')
def get_random_object(sequence, count=1):
    """
    Return a list of `count` random objects selected from the given sequence.

    Arguments:
        sequence (list): A sequense of any objects.
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
def get_same_object(sequence, related_name):
    """
    Return a list of objects that share at least one category with the items in the sequence,
    but are not themselves in the sequence.

    Arguments:
        sequence (list): A sequense of any objects.
        related_name (str): A related_name for reverse relation.

    Returns:
        same_object (list): List of objects that are similar in category from sequence.
    """

    same_object = set()
    for item in sequence:
        for category in item.categories.all():
            same_object.update(getattr(category, related_name).all())

    same_object = list(same_object - set(sequence))

    return same_object
