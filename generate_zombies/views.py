from django.shortcuts import render

# Create your views here.

def generateZombies(request):
    return render(request, 'generate_zombies/generate.html')