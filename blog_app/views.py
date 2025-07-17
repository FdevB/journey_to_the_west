from django.shortcuts import render

# Create your views here.
def blog_view(request):
    return render(request, 'blog_app/blog.html')

def blog_detail_view(request):
    return render(request, 'blog_app/blog_detail.html')
