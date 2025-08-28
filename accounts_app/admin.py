from django.contrib import admin

from accounts_app.models import ProfileModel, GradeModel


# Register your models here.
@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'birth_day']
    # readonly_fields = ['grade']

@admin.register(GradeModel)
class GradeModelAdmin(admin.ModelAdmin):
    list_display = ['grader', 'target_profile', 'score']
    list_filter = ['target_profile']
