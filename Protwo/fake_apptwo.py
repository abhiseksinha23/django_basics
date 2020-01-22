import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'Protwo.settings'

import django
django.setup()

import random
from apptwo.models import User
from faker import Faker

fakegen = Faker()


def populate(n=5):
    for entry in range(n):
        fake_first = fakegen.first_name()
        fake_last = fakegen.last_name()
        fake_email = fakegen.email()


        user = User.objects.get_or_create(first_name=fake_first, last_name=fake_last,email=fake_email)[0]
if __name__ == '__main__':

    print("populating")
    populate(50)
    print("population done!")
