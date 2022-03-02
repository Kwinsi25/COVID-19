from django.shortcuts import render
from home.models import *

# Create your views here.
def home(request):
    beds = Bed.objects.all()
    bedcnt = 0
    for bed in beds:
        if bed.occupied == False:
            bedcnt = bedcnt + 1
    return render(request, 'index.html',{"bedcnt":bedcnt,"beds":beds})

def login(request):
    return render(request,'login.html')
