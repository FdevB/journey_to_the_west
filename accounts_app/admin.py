from django.contrib import admin

from accounts_app.models import ProfileModel

# Register your models here.
@admin.register(ProfileModel)
class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone', 'birth_day']
