import os
import subprocess
from django_doc import main
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Collecting Docstrings of Project'

    def handle(self, *args, **options):
        main.run('/home/ali/dev/bonus-core/')
        self.stdout.write(self.style.SUCCESS('Documentation Collected Successfully.'))
