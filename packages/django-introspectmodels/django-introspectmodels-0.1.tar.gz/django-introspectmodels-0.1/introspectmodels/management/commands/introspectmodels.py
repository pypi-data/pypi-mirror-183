import json

from django.core.management.base import BaseCommand

from introspectmodels.introspect_utils.models_introspector import ModelIntrospector  # noqa:E501


class Command(BaseCommand):
    help = 'Introspect models of your project'

    def add_arguments(self, parser):
        parser.add_argument(
            "--output-file",
            default=None,
            help="json output file for introspected models. default: print to stdout"  # noqa:E501
        )

    def handle(self, *args, **options):
        introspector = ModelIntrospector()
        introspector.introspect_models()

        output = introspector.get_output()
        if options["output_file"] is None:
            print(json.dumps(output, indent=4))
        else:
            with open(options["output_file"], 'w') as fout:
                # indent=4 because it will be read by human
                json.dump(output, fout, indent=4)
