from django.urls import path
from .views import matiere, createMatiere, updateMatiere, deleteMatiere

urlpatterns = [
    path('', matiere, name="matiere"),
    path('create-matiere/', createMatiere, name="create-matiere"),
]