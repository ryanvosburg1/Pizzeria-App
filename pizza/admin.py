from django.contrib import admin
from .models import Topping

# Register your models here.

from .models import Pizza

admin.site.register(Pizza)
admin.site.register(Topping)

