import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizzeria.settings")

import django
django.setup()

from learning_logs.models import Pizza

pizzas = pizza.objects.all()

for p in pizzas:
    print(pizza.id, topic)




