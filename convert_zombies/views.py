from django.shortcuts import render

# Create your views here.
def convertZombies(request):
    return render(request, 'convert_zombies/convert.html')