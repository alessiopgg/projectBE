import json
from django.core.management import call_command
from django.core.serializers.json import DjangoJSONEncoder
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projectBE.settings")

import django
django.setup()

with open('db.json', 'w', encoding='utf-8') as outfile:
    call_command('dumpdata', format='json', indent=2, stdout=outfile)
