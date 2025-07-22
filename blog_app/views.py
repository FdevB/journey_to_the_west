from django.shortcuts import render, get_object_or_404

from blog_app.models import PostModel

# Create your views here.
def blog_view(request):
    """
    View for handling requests to the /blog/ endpoint for PostModel.

    This view manages listing PostModel instances.

    Args:
        request (HttpRequest): Required arguments for views.

    Variables:
        posts (QuerySet[PostModel]): All posts retrieved from the database.
        template_name (str): Path to the template file.
        context (dict): Context data sent to the template.
    
    Returns:
        HttpResponse: Rendered HTML response with context data.
    """

    posts = PostModel.objects.filter(status=1)

    template_name = 'blog_app/blog.html'
    context = {
        'posts': posts,
    }
    return render(request, template_name, context)

def blog_detail_view(request, slug):
    """
    View for handling requests to the /blog/detail/<slug> endpoint for PostModel.

    This view show the given object from PostModel.

    Args:
        request (HttpRequest): Required arguments for views.
        slug (str): a given slug from url.

    Variables:
        post (PostModel or 404): Retrieved post object matching the slug.
        template_name (str): Path to the template file.
        context (dict): Context data sent to the template.
    
    Returns:
        HttpResponse: Rendered HTML response with context data.
    """

    post = get_object_or_404(PostModel, slug=slug)

    template_name = 'blog_app/blog_detail.html'
    context = {
        'post': post
    }
    return render(request, template_name, context)
