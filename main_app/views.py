from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormMixin
from .models import Animal
from .forms import FunFactForm
# Create your views here.


def home(request):
    return render(request, 'home.html')


class AnimalDelete(DeleteView):
    model = Animal
    success_url = "/animals/"


class AnimalUpdate(UpdateView):
    model = Animal
    fields = "__all__"


class AnimalList(ListView):
    model = Animal


class AnimalCreate(CreateView):
    model = Animal
    fields = "__all__"


class AnimalDetail(FormMixin, DetailView):
    model = Animal
    form_class = FunFactForm


def animal_detail(request, animal_id):
    animal = Animal.objects.get(id=animal_id)
    # Get the toys the cat doesn't have
#   toys_cat_doesnt_have = Toy.objects.exclude(id__in = cat.toys.all().values_list('id'))
    funfact_form = FunFactForm()
    return render(request, 'animals/detail.html', {
        'animal': animal, 'funfact_form': funfact_form,
        # Add the toys to be displayed
        # 'toys': toys_cat_doesnt_have
    })


def about(request):
    return render(request, 'about.html')


def signup(request):
    error_message = ''
    if request.method == 'POST':
        # This is how to create a 'user' form object
        # that includes the data from the browser
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # This will add the user to the database
            user = form.save()
            # This is how we log a user in via code
            login(request, user)
            return redirect('animal_index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)


def add_funfact(request, animal_id):
    if request.method == 'POST':
        factform = FunFactForm(request.POST)
        if factform.is_valid():
            new_fact = factform.save()
            new_fact.animal_id = animal_id
            new_fact.save()
    return redirect('animal_detail', animal_id=animal_id)
