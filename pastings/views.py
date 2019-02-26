from django.shortcuts import render
from .models import Pastings

# Create your views here.
def home(request):
    pastings = Pastings.objects
    return render(request, 'pastings/home.html', {'pastings':pastings})
