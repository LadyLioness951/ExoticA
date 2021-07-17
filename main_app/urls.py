from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('animals/', views.AnimalList.as_view(), name="animals_index"),
    path('animals/create/',views.AnimalCreate.as_view(), name="animals_create"),
    path('animals/<int:pk>/', views.AnimalDetail.as_view(), name="animal_detail"),

    path('account/signup/', views.signup, name="signup")
]
