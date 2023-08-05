import logging

from django.apps import apps
from django.apps import AppConfig
from django.db.models import Model
from django.db.transaction import connections


LOGGER = logging.getLogger()


class ModelIntrospector:
    def __init__(self):
        self._introspected_data = {"apps": []}
        self.connection = None

    def _check_connections(self):
        self.connection = connections.all()[0]
        if len(connections.all()) > 1:
            LOGGER.warning("cannot work with multiple database projects, assuming 'default is the one to use'")  # noqa: E501
            for con in connections.all():
                if con.alias == "default":
                    self.connection = con
                    break
            else:
                databases_name = [c.alias for c in connections.all()]
                LOGGER.warning(
                    f"cannot found a database named default in your multiple database settings. Founds : {', '.join(databases_name)}"  # noqa: E501
                )
                self.connection = None

    def introspect_models(self):
        self._check_connections()
        self.introspect_apps_with_model()

    def introspect_apps_with_model(self):
        for app_config in apps.get_app_configs():
            # ignore apps with no models
            if len(list(app_config.get_models())) == 0:
                continue

            self._introspected_data["apps"].append({
                "app_name": app_config.name,
                "models": self.get_introspect_app_models(app_config),
            })

    def get_introspect_app_models(self, app_config: AppConfig) -> list[dict]:
        ret = []
        for model in app_config.get_models():
            introspected_fields = self.get_introspected_model_fields(model)
            ret.append({
                "model_name": model.__name__,
                "fields": introspected_fields
            })
        return ret

    def get_introspected_model_fields(self, model: Model) -> list[dict]:
        ret = []

        for field in model._meta.get_fields():
            ret_field = {
                "field_name": field.name,
                "field_type": field.__class__.__name__,
                "is_nullable": field.null,
                "is_relation": field.is_relation,
            }
            if self.connection is not None:
                ret_field["db_type"] = field.db_type(self.connection)
            else:
                ret_field["db_type"] = None

            if field.is_relation:
                ret_field.update({
                    "related_model": field.related_model.__name__,
                    "unique_constraint": None,
                    "is_primary_key": None,
                    "verbose_name": None,
                })
            else:
                ret_field.update({
                    "unique_constraint": field.unique,
                    "is_primary_key": field.primary_key,
                    # str() is needed for proxy fields
                    "verbose_name": str(field.verbose_name),
                    "related_model": None,
                })

            ret.append(ret_field)
        return ret

    def get_output(self):
        """ method is here if we need modification of the introspected data in the future
        """
        return self._introspected_data
