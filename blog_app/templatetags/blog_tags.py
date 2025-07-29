from django import template
from django.template.defaultfilters import stringfilter

import random


register = template.Library()

@register.filter(name='get_random')
def get_random_objects(sequence, count=1):
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
def get_same_objects(sequence, related_name, kind='c'):
    """
    Return a list of objects that share at least one category with the items in the sequence,
    but are not themselves in the sequence.

    Arguments:
        type (str): Select subscription type.
        sequence (list): A sequense of any objects.
        related_name (str): A related_name for reverse relation.

    Returns:
        types (dict): All selected modes for the subscription type
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


# @register.inclusion_tag()
# def get_last_objects(sequence, count):
#     pass
