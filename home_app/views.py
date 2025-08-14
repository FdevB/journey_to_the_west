from django.shortcuts import render

from blog_app.models import PostModel

# Create your views here.
def home_view(request):
    """
    View for handling requests to the / endpoint.

    This view show the template.

    Arguments:
        request (HttpRequest): Required arguments for views.

    Variables:
        template_name (str): Path to the template file.

    Returns:
        HttpResponse: Rendered HTML response with context data.
    """

    a = PostModel.objects.filter(pk=4)

    template_name = 'home_app/index.html'
    return render(request, template_name, {'a': a})
