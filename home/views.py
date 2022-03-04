from django.forms import ModelForm
from django.shortcuts import redirect, render
<<<<<<< HEAD
from home.models import staff,Bed,Ward
=======
from home.models import staff,Bed,Oxygen
>>>>>>> 77daea6bdf86842d65596f8f41ee2ece8a9de728

data ={}
def firstNameCheck(value):
    errorMessage = ""
    if value == "":
        errorMessage = "User name field is empty"
    return errorMessage,value
def passwordCheck(value):
    errorMessage = ""
    if value == "":
        errorMessage = "Password field is empty"
    return errorMessage,value
# Create your views here.
def home(request):
    oxy = Oxygen.objects.all()
    beds = Bed.objects.all()
    wards = Ward.objects.all()
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
               
<<<<<<< HEAD
    return render(request, 'index.html',{"bedcnt":bedcnt,"beds":beds,"wards":wards})
=======
    return render(request, 'index.html',{"bedcnt":bedcnt,"beds":beds,"oxy":oxy})
>>>>>>> 77daea6bdf86842d65596f8f41ee2ece8a9de728

def login(request):
    return render(request,'login.html')

def bedAvailablity(request):
    beds = Bed.objects.all() 
    return render(request, 'bedAvailablity.html',{"beds":beds})

def staffDashboard(request):
    return render(request,'staffDashboard.html')

def index(request):
    response = redirect('/home/')
    return response

def patient(request):
    return render(request, 'addPatient.html')