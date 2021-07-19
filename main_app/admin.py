from django.contrib import admin
from .models import Animal, FunFact, Photo

# Register your models here.
admin.site.register(Animal)
admin.site.register(FunFact)
admin.site.register(Photo)