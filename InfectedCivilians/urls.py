from .views import displayInfectedCivilians
from django.urls import path, include

urlpatterns = [
    # ...
    path('', displayInfectedCivilians, name='displayInfectedCivilians'),
]
