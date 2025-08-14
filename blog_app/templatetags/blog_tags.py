from django import template
from django.contrib.auth.models import User

from blog_app.models import PostModel, CategoryModel, TagModel

import random
import re


register = template.Library()

@register.filter(name='get_random')
def get_random_objects(sequence, count=1):
    """
    Return a list of 'count' random objects selected from the given sequence.

    Arguments:
        sequence (list): A sequence of any objects.
        count (int): Number of random items to return.

    Returns:
        random_objects (list): List of random object from sequence.
    """

    sequence = list(sequence)
    count = min(count, len(sequence))
    random_objects = random.sample(sequence, k=count)

    return list(random_objects)


@register.simple_tag(name='get_same')
def get_same_objects(sequence, related_name, kind):
    """
    Return a list of objects that share at least one category with the items in the sequence,
    but are not themselves in the sequence.

    Arguments:
        sample_object (object): The first object from the sequence.
        field (field): Get field from sample_object with kind.
        kind (str): Select subscription type.
        sequence (queryset): A sequence of any objects.
        related_name (str): A related_name for reverse relation.

    Variable:
        types (dict): All selected modes for the subscription type.

    Returns:
        same_object (list): List of objects that are similar in category from sequence.
    """

    sample_object = sequence[0]
    field = sample_object._meta.get_field(kind)

    if not field.is_relation:
        return []

    sequence = sequence.prefetch_related(field.name)
    same_object = set()
    if field.many_to_many:
        for item in sequence:
            for common_ground in getattr(item,  field.name).all():
                same_object.update(getattr(common_ground, related_name).all())

    elif field.many_to_one:
        for item in sequence:
            user = getattr(item, field.name)
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


@register.filter(name='mark_similar')
def highlight_similar_parts(text, search_query):
    """
    Highlights parts of the given text that partially match words from the search query.

    This filter is useful for visualizing which parts of a string match user input in a search bar,
    especially when using partial or fuzzy search.

    Arguments:
        context (dict): Django template context containing a key named 'search', which holds a string of space-separated search terms.
        text (str): The text string in which the search matches will be highlighted.

    Variable:
        search_query (str): The search query extracted from the context.
        search_words (list[str]): The list of individual words from the 'search_query' string.
        original_words (list[str]): The original input text split into words.
        highlighted_text (list[str]): A mutable copy of 'original_words' used to apply changes.
        term (str): A single word from the 'search_words' list, representing the current search term.
        word (str): A single word from 'original_words', representing a word from the original text.
        longest_match (str): The longest prefix of 'term' that matches the beginning of 'word'.
        pattern (str): The incremental substring of 'term' used to find 'longest_match'.
        found_object (Match): The match object returned by 're.search' containing the location of the match.
        s, e (int): Start and end indices of the match inside 'word'.
        txt (str): The actual matched text inside 'word'.
        new_str (str): The new version of 'word' with the matched part wrapped in a span tag.

    Returns:
        str: A version of the input `text` where any substring partially matching words in the search query (minimum 3 characters) is wrapped in `<span class="highlight">...</span>` for visual emphasis.
    """
    
    if not search_query:
        return text
    

    search_words = search_query.split()
    original_words = text.split()

    highlighted_text = text.split()

    for term in search_words:
        for index, word in enumerate(original_words):
            longest_match = ''

            for i in range(1, len(term) + 1):
                pattern = term[:i]

                if re.search(pattern, word, flags=re.IGNORECASE):
                    longest_match = pattern
                
                else:
                    break
            
            if len(longest_match) > 2:
                found_object = re.search(longest_match, word, flags=re.IGNORECASE)
                s, e = found_object.span()
                txt = found_object.group()

                new_str = word[:s] + f'<span class="highlight">{txt}</span>' + word[e:]
                
                highlighted_text[index] = new_str


    highlighted_text = ' '.join(highlighted_text)

    return highlighted_text


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
