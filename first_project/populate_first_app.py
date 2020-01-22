import os

os.environ['DJANGO_SETTINGS_MODULE'] = 'first_project.settings'

import django
django.setup()

#fake pop script

import random
from first_app.models import AccessRecord,Topic,Webpage
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def  add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(n=5):
    for entry in range(n):
        #get a topic for entry
        top = add_topic()
        #create fake data for entry
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()
        #create the new webpage entry
        webpg = Webpage.objects.get_or_create(topic=top,urls=fake_url,name=fake_name)[0]
        #create a fake AccessRecord for that Webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':

    print("populating")
    populate(20)
    print("population done!")
