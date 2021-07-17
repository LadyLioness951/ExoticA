from django.db import models

# Create your models here.
DIETS = (('H', 'Herbivore'), ('C', 'Carnivore'), ('O', 'Omnivore'))

class Animal(models.Model):
    # diet endanger phylum(?) manytomanyfield(2) name
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    diet = models.CharField("Diet Type", 
        max_length=1,
        choices=DIETS,
        default=DIETS[0][0]
    )
    endangered = models.BooleanField()
