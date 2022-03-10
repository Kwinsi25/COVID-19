from django.forms import ModelForm
from django.shortcuts import redirect, render

from home.models import staff,Bed,Oxygen,Ward,Patient,Doctor,WardDoctor,Appointment,State,City
from django.http import JsonResponse
from django.core.mail import send_mail

from django.db.models import F


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
    wards = Ward.objects.all()
    beds = Bed.objects.all()
    doctors = WardDoctor.objects.all()
    states = State.objects.all()
    cities = City.objects.all()
    return render(request, 'addPatient.html',{"wards":wards,"beds":beds,"doctors":doctors,"states":states,"cities":cities})

def bookAppointment(request):
    if request.method == 'POST':
        patientCheck = request.POST.get('check')
        print(patientCheck)
        if patientCheck == "oldPatient":
            caseNumber = request.POST['caseNumber']
            if caseNumber != '':
                patient = Patient.objects.all().filter(caseNumber = caseNumber)
                if patient is not None:
                    for p in patient:
                        patientDetails = {}
                        patientDetails['pname'] = p.patientName
                        patientDetails['pphone'] = p.phone
                        patientDetails['pgender'] = p.gender
                        patientDetails['rphone'] = p.patientRelativeNumber
                        patientDetails['rname'] = p.patientRelativeName
                        patientDetails['pemail'] = p.patientEmail
                        patientDetails['caseNumber'] = p.caseNumber
                    return render(request,'bookAppointment.html',context=patientDetails)
                else:
                    return redirect ('/bookAppointment')
        elif patientCheck == "newPatient":
            return redirect ('/bookAppointment')
        else:
            return redirect ('/')

    return render(request,'bookAppointment.html')

def bookedAppointment(request):
    data = {}
    if request.method == 'POST':
        caseNumber = request.POST.get('caseNumber')
        if caseNumber == '':
            caseNumber = None
        patientName = request.POST['patientName']
        patientPhone = request.POST['patientPhone']
        gender = request.POST.get("gender")
        patientEmail = request.POST['emailId']
        relativeName = request.POST['relativeName']
        relativePhone = request.POST['relativePhone']
        reason = request.POST['reason']

        appointment = Appointment(caseNumber = caseNumber,patientName = patientName,patientEmail = patientEmail,gender = gender,phone = patientPhone,patientRelativeNumber = relativePhone,patientRelativeName = relativeName,reason=reason)
        appointment.save()
        data['sucess'] = "Your details are submitted you will get email from Hospital for Appointment Status"
        return render(request,'bookAppointment.html',context=data)

def viewPatient(request):
    return render(request, 'viewPatient.html')


    
def getbedsajax(request):
    if request.method == "POST":        
        wardname = request.POST['wardname']        
        try:
            beds = Bed.objects.all().filter(wardName=wardname,occupied=False)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(beds.values('bedId', 'bedNumber')), safe = False)

def getpricesajax(request):
    if request.method == "POST":        
        wardname = request.POST['wardname']  
        try:
            print(wardname)
            price = Ward.objects.all().filter(wardId=wardname)
            
            print(price.values('wardPrice'))
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)  
        return JsonResponse(list(price.values('wardName', 'wardPrice')), safe = False)        

def getdoctorsajax(request):
    if request.method == "POST":
        wardname = request.POST.get('wardname')
        try:
            doctors = WardDoctor.objects.all().filter(wardName=wardname)
            docs = []
            for row in doctors:
                docs.extend(list(Doctor.objects.filter(doctorId=row.doctorName_id)))
            doctord=Doctor.objects.all().filter(doctorName__in=docs)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(doctord.values('doctorId', 'doctorName')), safe = False)

def getcitiesajax(request):

    if request.method == "POST":
        stateName = request.POST['statename']
        try:            
            cities = City.objects.all().filter(stateName=stateName)
        except Exception:
            data['error_message'] = 'error'
            return JsonResponse(data)
        return JsonResponse(list(cities.values('cityId', 'cityName')), safe = False)  

def email(request):
    if request.method=="POST":
        
        send_mail(
             request.POST['Sub'],
             request.POST['Msg'],
             'chmsdonotreply@gmail.com',
             ['ajpatel2468@gmail.com'],
             fail_silently=False,
        )
    return render(request,"email.html")      