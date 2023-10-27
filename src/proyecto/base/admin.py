from django.contrib import admin
from .models import Cmaquinas_virtuales, Ctopology
from .models import Ctopology, Cvirtual_machine

# Register your models here.
admin.site.register(Cmaquinas_virtuales)
admin.site.register(Ctopology)
admin.site.register(Cvirtual_machine)