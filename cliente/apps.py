# from django.apps import AppConfig


# class ClienteConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'cliente'

from django.apps import AppConfig

class ClienteConfig(AppConfig):
    name = 'cliente'

    def ready(self):
        import cliente.signals