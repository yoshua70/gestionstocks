from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('produits/', include('produits.urls')),
    path('matieres/', include('matieres.urls')),
    path('commandes/', include('commandes.urls')),
    path('clients/', include('clients.urls'))
]
