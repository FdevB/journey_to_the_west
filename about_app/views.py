from django.shortcuts import render

# Create your views here.
def about_view(request):
    """
    View for handling requests to the /about-us/ endpoint.

    This view show the template.

    Args:
        request (HttpRequest): Required arguments for views.

    Variables:
        template_name (str): Path to the template file.

    Returns:
        HttpResponse: Rendered HTML response with context data.
    """

    template_name = 'about_app/about.html'
    return render(request, template_name)
