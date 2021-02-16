from django.core.management.base import BaseCommand
import os


class Command(BaseCommand):
    help = 'Para cambiar el nombre del proyecto'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='El nuevo nombre del proyecto')

    def handle(self, *args, **kwargs):
        new_project_name = kwargs['name']

        files_to_renames = [
            'boilerplate1/settings/base.py',
            'boilerplate1/wsgi.py',
            'manage.py'
        ]

        folder_to_rename = 'boilerplate1'
        for f in files_to_renames:
            with open(f, 'r') as file:
                filedata = file.read()
            filedata = filedata.replace('boilerplate1', new_project_name)
            with open(f, 'w') as file:
                file.write(filedata)
        os.rename(folder_to_rename, new_project_name)
        self.stdout.write(self.style.SUCCESS('El nombre del proyecto a sido cambiado por: ' + new_project_name))
