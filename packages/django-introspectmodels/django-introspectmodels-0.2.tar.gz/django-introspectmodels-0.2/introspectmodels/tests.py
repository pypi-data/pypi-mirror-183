import os

from django.test import TestCase
from django.conf import settings
from django.apps import apps
from django.core.management import call_command

from introspectmodels.introspect_utils.models_introspector import ModelIntrospector  # noqa: E501
from music.models import Song


def is_in_list(lst: list, field_name: str, value):
    for item in lst:
        if item[field_name] == value:
            return True
    return False


class ModelIntrospectorTest(TestCase):
    def setUp(self) -> None:
        self.introspector = ModelIntrospector()

    def test_check_connections(self):
        self.introspector._check_connections()
        self.assertNotEqual(self.introspector.connection, None)

    def test_get_introspected_model_fields(self):
        introspected_fields = self.introspector.get_introspected_model_fields(Song)  # noqa E501
        self.assertTrue(is_in_list(introspected_fields, "field_name", "title"))
        self.assertTrue(is_in_list(introspected_fields, "field_name", "album"))
        self.assertTrue(is_in_list(introspected_fields, "field_name", "order"))
        self.assertTrue(is_in_list(introspected_fields, "field_name", "mp3_file"))  # noqa E501
        self.assertTrue(is_in_list(introspected_fields, "field_name", "id"))

    def test_get_introspect_app_models(self):
        app = apps.get_app_config('music')
        introspected_models = self.introspector.get_introspect_app_models(app)  # noqa E501
        self.assertTrue(is_in_list(introspected_models, "model_name", "Song"))
        self.assertTrue(is_in_list(introspected_models, "model_name", "Album"))
        self.assertTrue(is_in_list(introspected_models, "model_name", "Band"))

    def test_introspect_apps_with_model(self):
        self.introspector.introspect_apps_with_model()
        self.assertTrue(is_in_list(
            self.introspector._introspected_data["apps"],
            "app_name",
            "music"
        ))
        self.assertTrue(is_in_list(
            self.introspector._introspected_data["apps"],
            "app_name",
            "people"
        ))

    def test_launch_at_django_startup(self):
        json_schema_path = os.path.join(settings.BASE_DIR, ".forestadmin-schema.json")
        if os.path.exists(json_schema_path):
            os.remove(json_schema_path)

        manage_file_path = os.path.join(settings.BASE_DIR, "manage.py")
        os.system(f"python {manage_file_path} check")
        self.assertTrue(os.path.exists(json_schema_path))

    def test_get_output(self):
        self.introspector.introspect_apps_with_model()
        self.assertEqual(
            self.introspector._introspected_data,
            self.introspector.get_output()
        )

    def test_manage_command(self):
        json_schema_path = os.path.join(settings.BASE_DIR, ".forestadmin-schema.json")
        if os.path.exists(json_schema_path):
            os.remove(json_schema_path)

        call_command("introspectmodels", output_file=json_schema_path)
        self.assertTrue(os.path.exists(json_schema_path))
