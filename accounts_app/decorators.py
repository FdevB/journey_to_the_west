from django.shortcuts import redirect
from django.contrib import messages

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
    def _wrapper(request, *args, **kwargs):
        if request.user.is_anonymous:
            return function(request, *args, **kwargs)

        messages.warning(request, "You must log out of your account to access.")
        return redirect('home_app:home')
    
    return _wrapper


def role_required(role):
    """
    Decorator for views that should only be accessible by `ROLE` user.

    Arguments:
        role (list): Role required for access.

    Returns:
        _inner_decorator: A decorator that restricts access based on the user's role.
    """

    def _inner_decorator(function):

        @wraps(function)
        def _wrapper(request, *args, **kwargs):
            if request.user.profile.role in role:
                return function(request, *args, **kwargs)

            messages.warning(request, "Your role does not have access.")
            return redirect('home_app:home')

        return _wrapper

    return  _inner_decorator
