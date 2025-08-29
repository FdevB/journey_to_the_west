from django.db.models.expressions import result
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from blog_app.models import PostModel

# Create your views here.
def blog_view(request, **kwargs):
    """
    View for handling requests to the /blog/ endpoint for PostModel.

    This view manages listing PostModel instances.
    If the current site domain is localhost, the site will show the preview to the admin.

    Arguments:
        request (HttpRequest): Required arguments for views.
        kwargs (dict): Key, value for extra optional arguments.

    Variables:
        posts (QuerySet[PostModel]): All posts retrieved from the database or filtered based on needs.
        template_name (str): Path to the template file.
        context (dict): Context data sent to the template.
    
    Returns:
        HttpResponse: Rendered HTML response with context data.
    """

    posts = PostModel.objects.filter(status='published')
    search = None

    result = "Read about this journey here"
    if category := kwargs.get('category_name'):
        posts = posts.filter(categories__slug=category)
        result = f"result for {category} category"
    
    elif tag := kwargs.get('tag_name'):
        posts = posts.filter(tags__slug=tag)
        result = f"result for {tag} tag"
    
    elif author := kwargs.get('author_name'):
        posts = posts.filter(author__username=author)
        result = f"result for {author} author"

    elif search := request.GET.get('search'):
        posts = posts.filter(title__icontains=search)
        result = f"result for {search} search"


    paginator = Paginator(posts, 5)
    page_number = request.GET.get('page', 1)
    page_objects = paginator.get_page(page_number)


    template_name = 'blog_app/blog.html'
    context = {
        'all_post': posts,
        'result': result,
        'search': search,
        'page_objects': page_objects,
    }
    return render(request, template_name, context)

@login_required()
def blog_detail_view(request, slug):
    """
    View for handling requests to the /blog/detail/<slug> endpoint for PostModel.

    This view show the given object from PostModel.
    And it adds one to the number of `views` to this site.

    Args:
        request (HttpRequest): Required arguments for views.
        slug (str): a given slug from url to display current post.

    Variables:
        post (PostModel or 404): Retrieved post object matching the slug.
        template_name (str): Path to the template file.
        context (dict): Context data sent to the template.
    
    Returns:
        HttpResponse: Rendered HTML response with context data.
    """

    post = get_object_or_404(PostModel, slug=slug)
    post.views += 1
    post.save()


    template_name = 'blog_app/blog_detail.html'
    context = {
        'post': post,
        'related_post': PostModel.objects.filter(id=post.id),
    }
    return render(request, template_name, context)
