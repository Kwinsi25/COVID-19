from django.forms import ModelForm
from django.shortcuts import redirect, render
from home.models import staff,Bed,Oxygen,Ward,Patient,Doctor


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
            return render (request, 'staffDashboard.html',{'user':staffDetails.get()})
        else:
             err="Username and Password is not valid!"
    if request.method == 'POST':
        username = request.POST.get('username')
       

        password = request.POST.get('password') 
        
        doctorDetails=Doctor.objects.filter(doctorUsername = username, doctorPass= password)
        
        if doctorDetails.count() > 0 :
            return render (request, 'doctorDashboard.html',{'user':doctorDetails.get()})
        else:

            return render(request, 'index.html',{'err':err})
               
    return render(request, 'index.html',{"bedcnt":bedcnt,"beds":beds,"oxy":oxy,"wards":wards})

def login(request):
    return render(request,'login.html')

def bedAvailablity(request):
    beds = Bed.objects.all() 
    return render(request, 'bedAvailablity.html',{"beds":beds})

def staffDashboard(request):
    return render(request,'staffDashboard.html')

def doctorDashboard(request):
    return render(request,'doctorDashboard.html')

def index(request):
    response = redirect('/home/')
    return response

def patient(request):
    return render(request, 'addPatient.html')

def bookAppointment(request):
    if request.method == 'POST':
        patientCheck = request.POST.get('check')
        print(patientCheck)
        if patientCheck == "oldPatient":
            caseNumber = request.POST['caseNumber']
            patient = Patient.objects.all().filter(caseNumber = caseNumber)
            if patient is not None:
                for p in patient:
                    patientDetails = {}
                    patientDetails['pname'] = p.patientName
                    patientDetails['pphone'] = p.phone
                    patientDetails['pgender'] = p.gender
                    patientDetails['rphone'] = p.patientRelativeNumber
                    patientDetails['rname'] = p.patientRelativeName
                return render(request,'bookAppointment.html',context=patientDetails)
            else:
                return redirect ('/bookAppointment')
        elif patientCheck == "newPatient":
            return redirect ('/bookAppointment')
        else:
            return redirect ('/')

    return render(request,'bookAppointment.html')
def viewPatient(request):
    return render(request, 'viewPatient.html')
