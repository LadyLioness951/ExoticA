from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    path('animals/', views.AnimalList.as_view(), name="animals_index"),
    path('account/signup/', views.signup, name="signup")
]
