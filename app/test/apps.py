from django.apps import AppConfig  # noqa


class TestConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'test'
