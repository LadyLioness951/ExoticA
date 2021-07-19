from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

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

    def get_absolute_url(self):
        return reverse('animal_detail', kwargs={'pk': self.id})


class FunFact(models.Model):
    fact = models.TextField(max_length=2000)

# class Like(models.Model):
#     fun_fact = models.ForeignKey(FunFact, on_delete = models.CASCADE)
#     user = models.ForeignKey(User, on_delete = models.CASCADE)
