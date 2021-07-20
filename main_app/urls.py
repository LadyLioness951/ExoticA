from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('animals/', views.AnimalList.as_view(), name="animals_index"),
    path('animals/create/', views.AnimalCreate.as_view(), name="animals_create"),
    path('animals/<int:animal_id>/', views.animal_detail, name='animal_detail'),
    path('animals/<int:pk>/update/', views.AnimalUpdate.as_view(), name='animal_update'),
    path('animals/<int:pk>/delete/', views.AnimalDelete.as_view(), name='animal_delete'),


    path('animals/<int:animal_id>/add_photo/', views.add_photo, name='add_photo'),
    path('animals/<int:pk>/remove_photo/', views.RemovePhoto.as_view(), name='remove_photo'),

    path('animals/<int:animal_id>/add_funfact/', views.add_funfact, name="add_funfact"),
    path('animals/<int:animal_id>/funfacts/<int:funfact_id>/like/', views.like, name='like'),

    path('account/signup/', views.signup, name="signup"),
]
