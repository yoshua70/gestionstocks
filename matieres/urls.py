from django.urls import path
from . import views

urlpatterns = [
    path('', views.matiere, name="matieres"),
    path('create/', views.createMatiere, name="create-matiere"),
    path('details/<int:pk>', views.createMatiere, name="fiche-matiere"),
    path('delete/<int:pk>', views.deleteMatiere, name="delete-matiere"),
    path('update/<int:pk>', views.updateMatiere, name="update-matiere"),
]
