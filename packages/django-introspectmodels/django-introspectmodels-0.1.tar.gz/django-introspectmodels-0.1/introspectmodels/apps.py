import os

from django.apps import AppConfig
from django.conf import settings
from django.core.management import call_command


class IntrospectmodelsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "introspectmodels"

    def ready(self) -> None:
        output_file = os.path.join(settings.BASE_DIR, '.forestadmin-schema.json')
        call_command("introspectmodels", output_file=output_file)
