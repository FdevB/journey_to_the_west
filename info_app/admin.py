from django.contrib import admin

from info_app.models import MessageModel

# Register your models here.
@admin.register(MessageModel)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'is_read', 'sent_at']
    list_filter = ['name', 'email', 'is_read', 'sent_at']
