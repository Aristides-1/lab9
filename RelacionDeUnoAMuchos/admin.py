from django.contrib import admin
from .models import SimpleModel, Language, NullExample, Framework

admin.site.register(SimpleModel)
admin.site.register(Language)
admin.site.register(NullExample)
admin.site.register(Framework)