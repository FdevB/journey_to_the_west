from django.shortcuts import render
from django.views.generic.base import TemplateView

from blog_app.models import PostModel

# Create your views here.
class HomeView(TemplateView):
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

    template_name = 'home_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_post'] = PostModel.objects.all()[:3]
        return context
