from django.contrib import admin

from accounts_app.models import ProfileModel, GradeModel


# Register your models here.
@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    """
    Admin configuration for the ProfileModel.

    This class registers ProfileModel in the Django admin interface with all its features.

    Attributes:
        list_display (list[str]): Fields to display as columns in the list view.
    """

    list_display = ['user', 'phone', 'birth_day']


@admin.register(GradeModel)
class GradeModelAdmin(admin.ModelAdmin):
    """
    Admin configuration for the GradeModel.

    This class registers GradeModel in the Django admin interface with all its features.

    Attributes:
        list_display (list[str]): Fields to display as columns in the list view.
        list_filter (list[str]): Fields to filter by in the sidebar.
    """

    list_display = ['grader', 'target_profile', 'score']
    list_filter = ['target_profile']
