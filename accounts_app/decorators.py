from django.shortcuts import redirect

from functools import wraps


def logout_required(function):
    """
    Decorator for views that should only be accessible by `anonymous users`.

    Arguments:
        function (callable): The view function to apply the logout restriction to.

    Returns:
        Result of `function` or redirect user in `Home Page`
    """

    @wraps(function)
    def _wraps(request, *args, **kwargs):
        if request.user.is_anonymous:
            return function(request, *args, **kwargs)
            
        return redirect('home_app:home')
    
    return _wraps
