from django.conf import settings
from django.forms import ModelForm
from django.shortcuts import redirect, render

from home.models import PatientDocument, PatientSymptom, staff,Bed,Oxygen,Ward,Patient,Doctor,Symptoms,WardDoctor,Appointment,State,City,page,block,ContactUs
from django.http import JsonResponse
from django.core.mail import send_mail

from django.db.models import F
from datetime import date
from django.views.generic import DetailView

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string 
from django.utils.html import strip_tags

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
    slug = terms()
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
    
                return redirect ("doctorDashboard/")
        else:
            err="Username and Password is not valid!"
            return render(request, 'index.html',{'err':err})
               
    return render(request, 'index.html',{"bedcnt":bedcnt,"beds":beds,"oxy":oxy,"wards":wards,"recovered":recovered,"deceased":deceased,"slug":slug})

def login(request):
    return render(request,'login.html')

def patients(request):
    patientDetails = Patient.objects.all()
    return render(request, 'patient.html',{"patientDetails":patientDetails})

def bedAvailablity(request):
    beds = Bed.objects.all() 
    return render(request, 'bedAvailablity.html',{"beds":beds})

def staffDashboard(request):
    patientDetails = Patient.objects.all().order_by('dateTime')[:5]
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
   
    
    #patient=Patient.objects.all().filter(doctorName=Details.get())
    doctors = Doctor.objects.all()
    recovered = 0
    bedcnt = 0
    appointments = 0
    tappointments = 0
    username = None
    username = request.session["Duser"]
    docId=0
    for i in doctors:
        if i.doctorName==username:
            docId=i.doctorId

    print(date.today())

    patient = Patient.objects.all().filter(doctorName=docId)
    psp=Patient.objects.all().filter(doctorName=docId).order_by('-dateTime')[:5]
    for i in patient:
        if i.doctorVisitingTime==date.today():
            tappointments=tappointments+1
    for d in doctors:
        if d.doctorName == username:
            for p in patient:
                if d == p.doctorName:
                 
                    appointments = appointments + 1
                    if p.patientStatus == 'Recovered':
                        recovered = recovered + 1 
                        
    for bed in beds:
        if bed.occupied == False:
            bedcnt = bedcnt + 1
    return render(request,'doctorDashboard.html',{"patient":patient,"psp":psp,"bedcnt":bedcnt,"oxy":oxy,"recovered":recovered,"appointments":appointments,"tappointments":tappointments})
def allPatientDoc(request):
    doctors = Doctor.objects.all()
    username = None
    username = request.session["Duser"]
    docId=0
    for i in doctors:
        if i.doctorName==username:
            docId=i.doctorId
    psp = Patient.objects.all().filter(doctorName=docId)
    return render(request,"allPatientDoc.html",{"psp":psp})
def confirmationDetails(request):
    id = request.GET.get('id')
    bookAppointment = Appointment.objects.all().filter(appointmentId=int(id[:-1]))
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
        wardss = request.POST['wardss']        
        wardId = Ward.objects.get(wardId=wardss)
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
        patient = Patient(caseNumber=caseNumber,patientName=patientName,patientEmail=email,gender=gender,phone=phone,patientRelativeNumber=patientRelativeContactNumber,patientRelativeName=patientRelativeName,line1=line1,line2=line2,state=stateId,city=cityId,wardName=wardId,pincode=pincode,previousHistory=history,dob=dob,bedNumber=bedId,doctorName=doctorId,doctorNotes=notes,doctorVisitingTime=time,patientStatus=status)
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
            return redirect ('bookAppointment')
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
        # send_mail(
        #      "New Appointment",
        #      patientName+" trying to book an appointment",
        #      'chmsdonotreply@gmail.com',
        #      ['ajpatel2468@gmail.com'],
        #      fail_silently=False,
        # )

        msg = patientName + " trying to book an appointment"
        html_content = render_to_string("basic.html",{'title':'New Appointment','content':msg,'Name':'Admin','Uname':patientName,'gender':gender,'reason':reason})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "New",
            text_content,
            settings.EMAIL_HOST_USER,
            ['ajpatel2468@gmail.com'],
        )
        email.attach_alternative(html_content,"text/html")
        email.send()
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
            print(beds)
        except Exception as e:
            data['error_message'] = e
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
        
        # send_mail(
        #      request.POST['Sub'],
        #      request.POST['Msg'],
        #      'chmsdonotreply@gmail.com',
        #      ['ajpatel2468@gmail.com'],
        #      fail_silently=False,
        # )

        html_content = render_to_string("basic.html",{'title':'test Email','content':request.POST['Msg'],'Name':request.POST['Name']})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "testing",
            text_content,
            settings.EMAIL_HOST_USER,
            ['ajpatel2468@gmail.com'],
        )
        email.attach_alternative(html_content,"text/html")
        email.send()
    return render(request,"email.html")   

def deletePatient(request):
    id = request.GET.get('id')
    p = Patient.objects.get(patientId = id[:-1])
    p.delete()
    return redirect("/staffDashboard")

def deleteAppointment(request):
    id = request.GET.get('id')
    p = Appointment.objects.get(appointmentId = id[:-1])
    p.delete()
    return redirect("/message")

def updatePatient(request):
    id = request.GET.get('id')
    updatePatient = Patient.objects.all().filter(patientId=int(id[:-1]))
    patient = Patient.objects.all()
    wards = Ward.objects.all()
    beds = Bed.objects.all()
    doctors = WardDoctor.objects.all()
    states = State.objects.all()
    cities = City.objects.all()
    symptoms = Symptoms.objects.all()
    patientName = id[:-1]
    updateSymptoms = PatientSymptom.objects.all().filter(patientName=patientName)
    # for i in patient: 
    #     print("date",i.doctorLastVisited)
    var=[]
    for i in updateSymptoms:
        var.append(i.Symptoms.symptoms)
    return render(request,"updatePatient.html",{"updatePatient":updatePatient,"patient":patient,"wards":wards,"beds":beds,"doctors":doctors,"states":states,"cities":cities,"symptoms":symptoms,"updateSymptoms":updateSymptoms,"var":var})   

# def terms(request):
#     getdata = page.objects.all().values()
#     for i in getdata:
#         if i['fieldname'] == 'termsConditions' and i['status'] == 'enabled':
#             termConditions = i['body']
#             return render(request, 'index.html',{"termConditions":termConditions})
#     return redirect('/')

def terms():
    getdata = page.objects.all().values()
    for i in getdata:
        if i['fieldname'] == 'termConditions' and i['status'] == 'enabled':
            slug = i['slug']
            return slug
        elif i['fieldname'] == 'aboutUs' and i['status'] == 'enabled':
            slug = i['slug']
            return slug    
        else:
            return None

def aboutUs(request):
    slug = terms()
    getdata = block.objects.all().values()
    for i in getdata:
        if i['slug'] == 'dr1':
            dr1 = i['content']
        elif i['slug'] == 'dr2':
            dr2 = i['content']
        elif i['slug'] == 'dr3':
            dr3 = i['content']
        elif i['slug'] == 'covidServices':
            covidServices = i['content']
        elif i['slug'] == 'modernScience':
            modernScience = i['content']
        elif i['slug'] == 'entrustHealth':
            entrustHealth = i['content']    
                 
    return render(request, 'aboutUs.html',{"slug":slug,"dr1":dr1,"dr2":dr2,"dr3":dr3,"covidServices":covidServices,"modernScience":modernScience,"entrustHealth":entrustHealth})

def contactUs(request):
    slug = terms()
    getdata = block.objects.all().values()
    contectus = ContactUs.objects.all()
    for i in getdata:
        if i['slug'] == 'contact':
            contact = i['content']
        elif i['slug'] == 'email':
            email = i['content'] 
        elif i['slug'] == 'address':
            address = i['content']     
    name=""
    emailid=""
    msg=""
    if request.method == "POST":
        name = request.POST['name']
        emailid = request.POST['email']
        msg = request.POST['msg']

        html_content = render_to_string("contactusemail.html",{'title':'Hello Admin,','msg':request.POST['msg'],'Name':request.POST['name'],'Email':request.POST['email']})
        text_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            "testing",
            text_content,
            settings.EMAIL_HOST_USER,
            ['omipatel213@gmail.com'],
        )
        email.attach_alternative(html_content,"text/html")
        email.send()

        contactusform = ContactUs(contactName = name,contactEmail = emailid,contactMsg = msg)
        contactusform.save()
    return render(request, 'contactUs.html',{"slug":slug,"contact":contact,"email":email,"address":address,'name':name,'emailid':emailid,'Msg':msg})

class TC(DetailView):
    model = page
    context_object_name = 'page'
    template_name = "termsConditions.html"
    
def PatientUpdate(request):
    
   if request.method == 'POST':
        
        patientId = request.POST['id']  
        caseNumber = request.POST['caseNumber']
        patientName = request.POST['patientName']
        phone = request.POST['phone']
        email = request.POST['email']
        gender = request.POST['gender']
        patientRelativeName = request.POST['patientRelativeName']
        patientRelativeContactNumber = request.POST['patientRelativeContactNumber']
        line1 = request.POST['line1']
        line2 = request.POST['line2']
        wardss = request.POST['wardss']
        # wardId = Ward.objects.get(wardName=wardss)
        statess = request.POST['statess']
        # stateId = State.objects.get(stateName=statess)
        cities = request.POST['cities']
        cityId = City.objects.get(cityName=cities)
        pincode = request.POST['pincode']
        dob = request.POST['dob']
        history = request.POST['history']
        beds = request.POST['beds']
        bedId = Bed.objects.get(bedId=beds)
        prices = request.POST['prices']
        doctors = request.POST['doctors']
        # doctorId = Doctor.objects.get(doctorName=doctors)
        notes = request.POST['notes']
        time = request.POST['time']
        status = request.POST['status']
        file1 = request.POST.getlist('file1')
        
        Patient.objects.filter(patientId=patientId).update(caseNumber=caseNumber,patientName=patientName,patientEmail=email,gender=gender,phone=phone,patientRelativeNumber=patientRelativeContactNumber,patientRelativeName=patientRelativeName,line1=line1,line2=line2,state=statess,city=cityId,wardName=wardss,pincode=pincode,previousHistory=history,dob=dob,bedNumber=bedId,doctorName=doctors,doctorNotes=notes,doctorVisitingTime=time,patientStatus=status)
        
        for i in range(len(file1)):
            # patientId = Patient.objects.latest('patientId')
            # print("hjjsjsjvjs",patientId)
            # patientId = Patient.objects.get(patientName=patientName) 
            PatientDocument.objects.filter(patientName=patientId).update(patientName=patientId,document=file1[i])
            
        symptoms = request.POST.getlist('symptoms')
        PatientSymptom.objects.filter(patientName = patientId).delete()
        
        for i in symptoms:
            symptomsId = Symptoms.objects.get(symptomsId=int(i))
            patientId = Patient.objects.get(patientName=patientName)
            patientSymptoms = PatientSymptom(patientName=patientId,Symptoms=symptomsId)
            patientSymptoms.save()
            # PatientSymptom.objects.save(patientName=patientId,Symptoms=i)
        return redirect('/staffDashboard')      

def showBed(request):
    beds = Bed.objects.all()
    wards = Ward.objects.all()
    bedcnt = 0
    for bed in beds:
        if bed.occupied == False:
            bedcnt = bedcnt + 1
    return render(request, 'showBed.html',{"bedcnt":bedcnt,"beds":beds})