from django.contrib import admin
from .models import Animal, FunFact, Photo, Like, Video

# Register your models here.
admin.site.register(Animal)
admin.site.register(FunFact)
admin.site.register(Photo)
admin.site.register(Like)
admin.site.register(Video)