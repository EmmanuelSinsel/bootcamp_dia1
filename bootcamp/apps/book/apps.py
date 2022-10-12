from django.apps import AppConfig


class BookConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.book' #SE AÑADE APPS. PARA INDICAR LA CARPETA CONTENEDORA
