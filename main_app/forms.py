from django.forms import ModelForm
from .models import FunFact


class FunFactForm(ModelForm):
    class Meta:
        model = FunFact
        fields = ['fact']
