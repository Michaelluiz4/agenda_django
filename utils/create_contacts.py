import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTCS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    import faker

    from contact.models import Contact, Category

    # Contact.objects.all().delete()  # apagar todos os dados de Contact que eu já tinha criado
    Contact.objects.all().delete() # apaga todos os usuários que são fictiocios (mantendo o superusuario por exemplo)
    Category.objects.all().delete()     # apagar todos os dados da Category que eu já tinha criado

    fake = faker.Faker('pt-BR')
    categories = ['Amigos', 'Familía', 'Conhecidos']

    django_categories = [Category(name=name) for name in categories]

    for category in django_categories:
        category.save()
    
    django_contacts = []

    for _ in range(NUMBER_OF_OBJECTCS):
        profile = fake.profile()
        email = profile['mail']
        first_name, last_name = profile['name'].split(' ', 1)
        phone = fake.phone_number()
        date: datetime = fake.date_this_year()
        description = fake.text(max_nb_chars=100)
        category = choice(django_categories)

        django_contacts.append(
            Contact(
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                email=email,
                date=date,
                description=description,
                category=category,
            )
        )

    if len(django_contacts) > 0:
        Contact.objects.bulk_create(django_contacts)

