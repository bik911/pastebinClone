from django.shortcuts import render
from .models import Pastings
from django.shortcuts import redirect

# Create your views here.
def home(request):
    pastings = Pastings.objects
    return render(request, 'pastings/home.html', {'pastings':pastings})

def newPaste(request):
    if  request.user.is_authenticated:
        pastings = Pastings.objects
        return render(request, 'pastings/paste.html', {'pastings':pastings})
    else:
        return redirect('login')

def profile(request):
    pastings = Pastings.objects
    return render(request, 'pastings/profile.html', {'pastings':pastings})
