from django.shortcuts import render

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
