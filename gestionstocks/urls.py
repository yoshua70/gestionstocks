from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
<<<<<<< HEAD
    path('', include('base.urls')),
    path('matiere/', include('matiere.urls')),
=======
    path('produits/', include('produits.urls')),
    path('matieres/', include('matieres.urls'))
>>>>>>> de8943b1c6d5980c8aeae62bacd6828142451c5b
]
