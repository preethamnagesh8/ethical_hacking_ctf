from .views import convertZombies
from django.urls import path, include

urlpatterns = [
    # ...
    path('', convertZombies, name='convert_zombies'),
]
