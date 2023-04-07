from .views import generateZombies
from django.urls import path, include

urlpatterns = [
    # ...
    path('generate/', generateZombies, name='generate_zombies'),
]
