from django.shortcuts import render

# Create your views here.
def contact_view(request):
    """
    View for handling requests to the /contact-us/ endpoint.

    This view show the template.

    Args:
        request (HttpRequest): Required arguments for views.

    Variables:
        template_name (str): Path to the template file.

    Returns:
        HttpResponse: Rendered HTML response with context data.
    """
    
    template_name = 'contact_app/contact.html'
    return render(request, template_name)
