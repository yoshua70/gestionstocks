from django.urls import path
from . import views

urlpatterns = [
    path('', views.matiere, name="matieres"),
]
