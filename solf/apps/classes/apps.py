from django.apps import AppConfig


class ClassesConfig(AppConfig):
    name = 'classes'

    def ready(self):
        from solf.apps.classes import signals
