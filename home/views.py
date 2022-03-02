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
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        staffDetails=staff.objects.filter(staffUserName = username,staffPassword = password)
        if staffDetails.count() > 0 :
            return redirect ('/staffDashboard')
        else:
            print("Not Found")    
    return render(request, 'index.html',{"bedcnt":bedcnt})


def bedAvailablity(request):
    beds = Bed.objects.all() 
    return render(request, 'bedAvailablity.html',{"beds":beds})

def staffDashboard(request):
    return render(request,"staffDashboard.html")
