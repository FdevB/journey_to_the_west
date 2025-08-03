from django.shortcuts import render, redirect
from django.contrib import messages

from info_app.forms import MessageForm

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

    template_name = 'info_app/about.html'
    return render(request, template_name)


def contact_view(request):
    """
    View for handling requests to the /contact-us/ endpoint.

    This view displays the contact form, handles form submission,
    validates the input, and uses Django's messaging framework
    to display success or error messages.

    Args:
        request (HttpRequest): Required arguments for views.

    Variables:
        form (MessageForm): Instance of the ModelForm used to render and validate the contact message fields.
        template_name (str): Path to the template file.
        context (dict): Context data sent to the template.

    Returns:
        HttpResponse: Rendered HTML response with context data.
    """
    
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        
        if form.is_valid():
            form.save()

            messages.success(request, "Your message was sent successfully.")
            return redirect("info_app:contact-us")
        
        messages.error(request, "There was a problem sending your message, please try again.")


    template_name = 'info_app/contact.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)

