from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from accounts_app.forms import GradeForm, SignupForm, ChangeUserDetailForm, ChangeUserProfileForm
from accounts_app.decorators import logout_required


# Create your views here.
@logout_required
def signup_view(request):
    """
    View for handling requests to the /sign-up/ endpoint for SignupForm.

    This view manages user registration.
    If the form is valid, a new user is created, logged in automatically,
    and redirected to the home page.

    Arguments:
        request (HttpRequest): The HTTP request object.

    Variables:
        form (SignupForm): Bound or unbound form instance with user data.
        template_name (str): Path to the template file.
        context (dict): Context data sent to the template.

    Returns:
        HttpResponse: Rendered HTML response with the form for GET or invalid POST requests.
        HttpResponseRedirect: Redirects to `home_app:home` after successful signup.
    """

    form = SignupForm()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            messages.success(request, "Your account was created and you are logged in.")

            return redirect('home_app:home')


    template_name = 'accounts_app/signup.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)

@logout_required
def login_view(request):
    """
    View for handling requests to the /log-in/ endpoint for AuthenticationForm.

    This view manages user login with an optional "remember me" feature.
    If credentials are valid, the user is logged in and redirected to the home page.

    Arguments:
        request (HttpRequest): The HTTP request object.

    Variables:
        form (AuthenticationForm): Bound or unbound authentication form instance.

    Returns:
        HttpResponse: Rendered HTML response with the form for GET or invalid POST requests.
        HttpResponseRedirect: Redirects to 'home_app:home' after successful login.
    """

    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            request.session.set_expiry(0)
            if request.POST.get('remember'):
                request.session.set_expiry(2592000) # 30 * 24 * 60 * 60 | 30 days

            if user := authenticate(request, username=username, password=password):
                login(request, user)
                messages.success(request, "Logged in successfully.")
                return redirect('home_app:home')


    template_name = 'accounts_app/login.html'
    context = {
        'form': form
    }
    return render(request, template_name, context)

@login_required
def logout_view(request):
    """
    View for handling requests to the /log-out/ endpoint.

    This view manages logging out the currently authenticated user
    and redirects them to the home page.

    Arguments:
    request (HttpRequest): The HTTP request object.

    Returns:
    HttpResponseRedirect: Redirects to `home_app:home` after logging out.
    """

    logout(request)
    return redirect('home_app:home')

@login_required
def profile_view(request, username):
    target_user = get_object_or_404(User, username=username)
    scoring_form = None

    if not target_user.profile.my_grades.filter(grader=request.user):
        scoring_form = GradeForm()
        if request.method == 'POST':
            scoring_form = GradeForm(request.POST)
            if scoring_form.is_valid():
                grade = scoring_form.save(commit=False)
                grade.grader = request.user
                grade.target_profile = target_user.profile
                grade.save()
                return redirect('accounts_app:profile', username=username)

    template_name = 'accounts_app/profile.html'
    context = {
        'target_user': target_user,
        'form': scoring_form,
    }
    return render(request, template_name, context)

@login_required
def edit_profile_view(request, username):
    target_user = get_object_or_404(User, username=username)

    user_form = ChangeUserDetailForm(instance=target_user)
    profile_form = ChangeUserProfileForm(instance=target_user.profile)
    if request.method == 'POST':
        user_form = ChangeUserDetailForm(request.POST, instance=target_user)
        profile_form = ChangeUserProfileForm(request.POST, files=request.FILES, instance=target_user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save(commit=False)
            profile_form.user = target_user
            profile_form.save()

            messages.success(request, "Your profile Changed successfully.")
            return redirect('accounts_app:profile', username=username)

    template_name = 'accounts_app/edit_profile.html'
    context = {
        'target_user': target_user,
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, template_name, context)
