from django.shortcuts import render, get_object_or_404

from blog_app import models

# Create your views here.
def blog_view(request):
    posts = models.PostModel.objects.filter(status=1)

    template_name = 'blog_app/blog.html'
    context = {
        'posts': posts,
    }
    return render(request, template_name, context)

def blog_detail_view(request, slug):
    post = get_object_or_404(models.PostModel, slug=slug)

    template_name = 'blog_app/blog_detail.html'
    context = {
        'post': post
    }
    return render(request, template_name, context)
