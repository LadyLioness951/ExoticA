from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import Animal, FunFact, Photo, Like, Video
from .forms import FunFactForm
import boto3
import os
import uuid

from main_app import models
# Create your views here.


def home(request):
    photos = Photo.objects.all()
    return render(request, 'home.html', {'photos': photos})

def charity(request):
    return render(request, 'charity.html')

class AnimalDelete(LoginRequiredMixin, DeleteView):
    model = Animal
    success_url = "/animals/"


class AnimalUpdate(LoginRequiredMixin, UpdateView):
    model = Animal
    fields = ['name', 'species', 'family', 'diet', 'endangered']


class AnimalList(LoginRequiredMixin, ListView):
    model = Animal


class AnimalCreate(LoginRequiredMixin, CreateView):
    model = Animal
    fields = ['name', 'species', 'family', 'diet', 'endangered']

    def form_valid(self, form):
        # Assign the logged in user (self.request.user)
        form.instance.user = self.request.user  # form.instance is the cat
    # Let the CreateView do its job as usual
        return super().form_valid(form)

@login_required
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


@login_required
def add_funfact(request, animal_id):
    if request.method == 'POST':
        factform = FunFactForm(request.POST)
        if factform.is_valid():
            new_fact = factform.save(commit=False)
            animal = Animal.objects.get(id=animal_id)
            new_fact.animal = animal
            new_fact.user = request.user
            new_fact.save()
    return redirect('animal_detail', animal_id=animal_id)


class FunFactDelete(LoginRequiredMixin, DeleteView):
    model = FunFact

    def get_success_url(self):
        return reverse('animal_detail', kwargs={'animal_id': self.object.id})


@login_required
def add_photo(request, animal_id):
    # photo-file will be the "name" attribute on the <input>
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # build a unique filename keeping the image's original extension
        key = uuid.uuid4().hex[:6] + \
            photo_file.name[photo_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(photo_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Photo.objects.create(
                url=url, animal_id=animal_id, user=request.user)
        except:
            print('An error occurred uploading file to S3')
    return redirect('animal_detail', animal_id=animal_id)

@login_required
def add_video(request, animal_id):
    # photo-file will be the "name" attribute on the <input>
    video_file = request.FILES.get('video-file', None)
    if video_file:
        s3 = boto3.client('s3')
        # build a unique filename keeping the image's original extension
        key = uuid.uuid4().hex[:6] + \
            video_file.name[video_file.name.rfind('.'):]
        try:
            bucket = os.environ['S3_BUCKET']
            s3.upload_fileobj(video_file, bucket, key)
            url = f"{os.environ['S3_BASE_URL']}{bucket}/{key}"
            Video.objects.create(
                url=url, animal_id=animal_id, user=request.user)
        except:
            print('An error occurred uploading file to S3')
    return redirect('animal_detail', animal_id=animal_id)


class RemovePhoto(LoginRequiredMixin, DeleteView):
    model = Photo
    success_url = '/animals/'

class RemoveVideo(LoginRequiredMixin, DeleteView):
    model = Video
    success_url = '/animals/'

@login_required
def like(request, animal_id, funfact_id):
    # funfact = FunFact.objects.get(id=funfact_id)
    # funfact.like_set.create(fun_fact = funfact, user = request.user)
    # new_like, created = Like.objects.get_or_create(user=request.user, fun_fact_id=funfact_id)
    Like.objects.get_or_create(user=request.user, fun_fact_id=funfact_id)
    return redirect('animal_detail', animal_id=animal_id)


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
            return redirect('animals_index')
        else:
            error_message = 'Invalid sign up - try again'
    # A bad POST or a GET request, so render signup.html with an empty form
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

