from django.apps import AppConfig


class BlogAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog_app'
    verbose_name = 'blog'

    def ready(self):
        import blog_app.signals
