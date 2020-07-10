from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'folioapps.users'

    def ready(self):
        from . import signals
