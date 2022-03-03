from django.forms import ModelForm
from django.shortcuts import redirect, render
from home.models import staff,Bed


# Create your views here.
def home(request):
    beds = Bed.objects.all()
    bedcnt = 0
    for bed in beds:
        if bed.occupied == False:
            bedcnt = bedcnt + 1
    return render(request, 'index.html',{"bedcnt":bedcnt})

def login(request):
    return render(request,'login.html')

def bedAvailablity(request):
    beds = Bed.objects.all() 
    return render(request, 'bedAvailablity.html',{"beds":beds})
