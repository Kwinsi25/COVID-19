from django.forms import ModelForm
from django.shortcuts import redirect, render

from home.models import PatientDocument, PatientSymptom, staff,Bed,Oxygen,Ward,Patient,Doctor,Symptoms,WardDoctor,Appointment,State,City
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
    patients = Patient.objects.all() 
    recovered = 0
    deceased = 0
    bedcnt = 0
    for p in patients:
        if p.patientStatus == 'Recovered':
            recovered = recovered + 1
        elif p.patientStatus == 'Deceased':
            deceased = deceased + 1  
    for bed in beds:
        if bed.occupied == False:
            bedcnt = bedcnt + 1
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        if request.POST.get("role")=="Staff":
            Details=staff.objects.filter(staffUserName = username,staffPassword = password)
        if request.POST.get("role")=="Doctor":
            Details=Doctor.objects.filter(doctorUsername = username, doctorPass= password)
        if Details.count() > 0 :
            if request.POST.get("role")=="Staff":
                #print(staffDetails.get())
                if "Suser" in request.session:
                    del request.session["Suser"]
                request.session['Suser']=str(Details.get())
                return redirect ( 'staffDashboard/')
            
 
            if request.POST.get("role")=="Doctor":
                patient=Patient.objects.all().filter(doctorName=Details.get())
                if "Duser" in request.session:
                    del request.session["Duser"]
                request.session['Duser']=str(Details.get())
    
                return render ( request,'doctorDashboard.html',{'patient':patient})
        else:
            err="Username and Password is not valid!"
            return render(request, 'index.html',{'err':err})
               
    return render(request, 'index.html',{"bedcnt":bedcnt,"beds":beds,"oxy":oxy,"wards":wards,"recovered":recovered,"deceased":deceased})

def login(request):
    return render(request,'login.html')

def patients(request):
    patientDetails = Patient.objects.all()
    return render(request, 'patient.html',{"patientDetails":patientDetails})

def bedAvailablity(request):
    beds = Bed.objects.all() 
    return render(request, 'bedAvailablity.html',{"beds":beds})

def staffDashboard(request):
    patientDetails = Patient.objects.all()
    oxy = Oxygen.objects.all()
    beds = Bed.objects.all()
    recovered = 0
    deceased = 0
    bedcnt = 0
    for p in patientDetails:
        if p.patientStatus == 'Recovered':
            recovered = recovered + 1
        elif p.patientStatus == 'Deceased':
            deceased = deceased + 1
    for bed in beds:
        if bed.occupied == False:
            bedcnt = bedcnt + 1
    return render(request,'staffDashboard.html',{"bedcnt":bedcnt,"oxy":oxy,"patientDetails":patientDetails,"recovered":recovered,"deceased":deceased})

def doctorDashboard(request):  
    oxy = Oxygen.objects.all()
    beds = Bed.objects.all()
    doctors = Doctor.objects.all()
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    recovered = 0
    bedcnt = 0
    appointments = 0
    tappointments = 0
    username = None
    username = request.session["Duser"]
    print(username)
    for d in doctors:
        if d.doctorName == username:
            for p in patients:
                if d == p.doctorName:
                    print(d)
                    print(p.doctorName)
                    appointments = appointments + 1
                    if p.patientStatus == 'Recovered':
                        recovered = recovered + 1 
                        
    for bed in beds:
        if bed.occupied == False:
            bedcnt = bedcnt + 1
    return render(request,'doctorDashboard.html',{"bedcnt":bedcnt,"oxy":oxy,"recovered":recovered,"appointments":appointments,"tappointments":tappointments})

def confirmationDetails(request):
    id = request.GET.get('id')
    bookAppointment = Appointment.objects.all().filter(appointmentId=int(id[0]))
    wards = Ward.objects.all()
    beds = Bed.objects.all()
    doctors = WardDoctor.objects.all()
    states = State.objects.all()
    cities = City.objects.all()
    symptoms = Symptoms.objects.all()
    return render(request,'approved.html',{"bookAppointment":bookAppointment,"wards":wards,"beds":beds,"doctors":doctors,"states":states,"cities":cities,"symptoms":symptoms})

def confirmDetails(request):
    if request.method == 'POST':
        caseNumber = request.POST['caseNumber']
        patientName = request.POST['patientName']
        phone = request.POST['phone']
        email = request.POST['email']
        gender = request.POST['gender']
        patientRelativeName = request.POST['patientRelativeName']
        patientRelativeContactNumber = request.POST['patientRelativeContactNumber']
        line1 = request.POST['line1']
        line2 = request.POST['line2']
        statess = request.POST['statess']
        stateId = State.objects.get(stateId=statess)
        cities = request.POST['cities']
        cityId = City.objects.get(cityId=cities)
        pincode = request.POST['pincode']
        dob = request.POST['dob']
        history = request.POST['history']
        wardss= request.POST['wardss']
        beds = request.POST['beds']
        bedId = Bed.objects.get(bedId=beds)
        prices = request.POST['prices']
        doctors = request.POST['doctors']
        doctorId = Doctor.objects.get(doctorId=doctors)
        notes = request.POST['notes']
        time = request.POST['time']
        status = request.POST['status']
        file = request.POST.getlist('file')
        patient = Patient(caseNumber=caseNumber,patientName=patientName,patientEmail=email,gender=gender,phone=phone,patientRelativeNumber=patientRelativeContactNumber,patientRelativeName=patientRelativeName,line1=line1,line2=line2,state=stateId,city=cityId,pincode=pincode,previousHistory=history,dob=dob,bedNumber=bedId,doctorName=doctorId,doctorNotes=notes,doctorLastVisited=time,patientStatus=status)
        patient.save()
        for i in range(len(file)):
            patientId = Patient.objects.get(patientName=patientName) 
            patientDocument = PatientDocument(patientName=patientId,document=file[i])
            patientDocument.save()
        symptoms = request.POST.getlist('symptoms')
        for i in symptoms:
            symptomsId = Symptoms.objects.get(symptomsId=int(i))
            patientId = Patient.objects.get(patientName=patientName)
            PatientSymptoms = PatientSymptom(patientName=patientId,Symptoms=symptomsId)
            PatientSymptoms.save()
        
        send_mail(
             "Appointment Booked",
             "Hello " + patientName + " your appointment is booked",
             'chmsdonotreply@gmail.com',
             [email],
             fail_silently=False,
        )
        return redirect ('/viewPatient')
        
    else:
        return render(request,'approved.html')    
def message(request):
    bookAppointment = Appointment.objects.all()
    return render(request,'confirmation.html',{"bookAppointment":bookAppointment})

def viewPatient(request):
    viewData = Patient.objects.all()
    return render(request, 'viewPatient.html',{"viewData":viewData})

def index(request):
    response = redirect('/home/')
    return response

def patient(request):
    wards = Ward.objects.all()
    beds = Bed.objects.all()
    doctors = WardDoctor.objects.all()
    states = State.objects.all()
    cities = City.objects.all()
    symptoms = Symptoms.objects.all()
    return render(request, 'addPatient.html',{"wards":wards,"beds":beds,"doctors":doctors,"states":states,"cities":cities,"symptoms":symptoms})


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
        send_mail(
             "New Appointment",
             patientName+" trying to book an appointment",
             'chmsdonotreply@gmail.com',
             ['ajpatel2468@gmail.com'],
             fail_silently=False,
        )
        data['sucess'] = "Your details are submitted you will get email from Hospital for Appointment Status"
        return redirect ('/',context=data)



def logout(request):
    try:
        del request.session['Suser']
        
        
    except KeyError:
      
        try:
            del request.session['Duser']
        except KeyError:
            pass
        
    return redirect ('/')
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

def updatePatient(request):
    id = request.GET.get('id')
    updatePatient = Patient.objects.all().filter(patientId=int(id[0]))
    patient = Patient.objects.all()
    wards = Ward.objects.all()
    beds = Bed.objects.all()
    doctors = WardDoctor.objects.all()
    states = State.objects.all()
    cities = City.objects.all()
    symptoms = Symptoms.objects.all()
    return render(request,"updatePatient.html",{"updatePatient":updatePatient,"patient":patient,"wards":wards,"beds":beds,"doctors":doctors,"states":states,"cities":cities,"symptoms":symptoms})   