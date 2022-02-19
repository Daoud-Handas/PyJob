from django.apps import AppConfig


class JobsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Jobs'

    def ready(self):
        from .tasks.scheduler import schedule
        schedule()