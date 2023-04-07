from django.shortcuts import render
from .models import InfectedCivilian
import base64, json
import logging
import pickle

# Create your views here.
def displayInfectedCivilians(request):
    if 'InfectedCookie' in request.COOKIES:
        cookieData = request.COOKIES.get('InfectedCookie')
        decoded_cookieData = base64.b64decode(cookieData)
        cookie_data = pickle.loads(decoded_cookieData)

    infected_civilians = InfectedCivilian.objects.all()
    return render(request, 'InfectedCivilian/infected_list.html', {'infected_civilians': infected_civilians})