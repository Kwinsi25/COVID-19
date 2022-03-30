from django.utils.timezone import now
from django.core.exceptions import ValidationError
import random
from django.db import models
from tinymce import models as tinymce_models
from django.urls import reverse

class configuration(models.Model):
    configurationId = models.AutoField(primary_key=True)
    label = models.CharField(max_length=10)
    fieldname = models.CharField(max_length=10,unique=True,default=None)
    value = models.IntegerField()

    def __str__(self):
        return str(self.label)

class page(models.Model):
    pageId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    fieldname = models.CharField(max_length=100,unique=True,default=None)
    slug = models.SlugField(null=True, unique=True)
    content = tinymce_models.HTMLField()
    statusChoice = (
        ('enabled','Enabled'),
        ('disabled','Disabled'),
    )
    status = models.CharField(max_length=10,choices=statusChoice,default='enabled')
    

    def __str__(self):
        return str(self.title)   

    def get_absolute_url(self):
        return reverse("termsConditions", kwargs={"slug": self.slug})    
        

class block(models.Model):
    blockId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100,unique=True,default=None)
    content = tinymce_models.HTMLField()
    statusChoice = (
        ('enabled','Enabled'),
        ('disabled','Disabled'),
    )
    status = models.CharField(max_length=10,choices=statusChoice,default='enabled')

    def __str__(self):
        return str(self.title) 

class staff(models.Model):
    staffId = models.AutoField(primary_key=True,default=None)
    staffUserName = models.CharField(max_length=24,default=None)
    staffMiddleName = models.CharField(max_length=24,default=None)
    staffLastName = models.CharField(max_length=24,default=None)
    staffPassword = models.CharField(max_length=24,null=True,blank=True)
    staffContactNumber = models.CharField(max_length=10)
    staffPhoto = models.ImageField(upload_to='staffImages',null=True, blank=True)
    genderChoice = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=genderChoice,default='M')
    statusChoice = (
        ('active','Active'),
        ('on_leave','On_leave'),
    )
    status = models.CharField(max_length=10,choices=statusChoice,default='active')
    
    def __str__(self):
        return self.staffUserName

class Ward(models.Model):
    wardId = models.AutoField(primary_key=True)
    wardName = models.CharField(("Ward Name"),max_length=10)
    wardPrice = models.DecimalField(("Ward Price"),max_digits=8,decimal_places=2,default=0.00)

    def __str__(self):
        return self.wardName
         
class Bed(models.Model):
    bedId = models.AutoField(primary_key=True)
    wardName = models.ForeignKey('Ward',on_delete=models.CASCADE,max_length=5,default=None)
    bedNumber = models.CharField(("Bed Number"),max_length=5)
    occupied = models.BooleanField(("Occupied"),default=False)
    
    def __str__(self):
        return str(self.wardName) +" - "+ str(self.bedNumber)

class Specialization(models.Model):
    specializationId = models.AutoField(primary_key=True)
    specialization = models.CharField(("Specialization"),max_length=64)

    def __str__(self):
        return self.specialization

class Doctor(models.Model):
    doctorId = models.AutoField(primary_key=True)
    doctorName = models.CharField(("Doctor Name"),max_length=24)
    doctorUsername=models.CharField(("Doctor Username"),max_length=15)
    doctorPass=models.CharField(("Doctor Password"),max_length=100)
    doctorContact = models.IntegerField(("Doctor Contact"))
    Specialization = models.ForeignKey('Specialization',on_delete = models.CASCADE,null=False)

    def __str__(self):
        return self.doctorName

class Equipment(models.Model):
    equipment_Id = models.AutoField(primary_key=True)
    equipment_Name = models.CharField(max_length=50)
    equipment_Quantity = models.IntegerField()
    equipment_Assigned = models.IntegerField()
    equipment_Usable = models.IntegerField()
    
    def __str__(self):
        return str(self.equipment_Name)


class Oxygen(models.Model):
    oxygen_Total = models.IntegerField(help_text = " Days &")
    oxygen_Total_Hour = models.TimeField(help_text = " Hours of Total Oxygen")
    oxygen_Used = models.IntegerField(help_text = " Days &")
    oxygen_Used_Hour = models.TimeField(help_text = " Hours of Oxygen Used")
    oxygen_Remaining = models.IntegerField(help_text = " Days &")
    oxygen_Remaining_Hour = models.TimeField(help_text = " Hours of Oxygen Remaining")

    def __str__(self):
        return str(self.oxygen_Remaining)

def validate_phoneNumber(value):
    if len(str(value)) == 10:
        return value
    else:
        raise ValidationError("please enter correct phonenumber with 10 digits")

def validate_pincode(value):
    if len(str(value)) == 6:
        return value
    else:
        raise ValidationError("please enter correct pincode with 6 digits")


# Create your models here.

class State(models.Model):
    stateId = models.AutoField(primary_key=True)
    stateName = models.CharField(("State Name"),max_length=24,unique=True)

    def __str__(self):
        return self.stateName

class Patient(models.Model):
    caseNumber = models.IntegerField(('Case Number'),default=random.randint(100000,999999),unique=True)
    patientId = models.AutoField(primary_key=True)
    patientName = models.CharField(("Patient Name"),max_length=24)
    patientEmail = models.EmailField(("Email Id"),unique=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.IntegerField(("Phone Number"),validators=[validate_phoneNumber],unique=True)
    patientRelativeNumber = models.IntegerField(("Relative's Phone number"),validators=[validate_phoneNumber])
    patientRelativeName = models.CharField(("Relative's name"),max_length=24)
    line1 = models.CharField(("Address line1"),max_length=250)
    line2 = models.CharField(("Address line2"),max_length=250)
    state = models.ForeignKey('State',on_delete=models.CASCADE,null=True)
    
    sname = State.objects.filter(stateName = state)
    city = models.ForeignKey('City',on_delete=models.CASCADE,null=True) #,limit_choices_to={'stateName': 1}
    pincode = models.IntegerField(("Pincode"),validators=[validate_pincode])
    previousHistory = models.CharField(("Previous history"),max_length=250)
    dob = models.DateField(("Date of birth"))
    wardName = models.ForeignKey('Ward',on_delete=models.CASCADE,blank=True,default="")
    bedNumber  = models.ForeignKey('Bed',on_delete=models.CASCADE,blank=True) #,limit_choices_to={'occupied': False}
    doctorName = models.ForeignKey('Doctor',on_delete=models.CASCADE,default=None,blank=True)
    doctorNotes = models.CharField(("Doctor Notes"),max_length=250,default=None,blank=True)
    doctorLastVisited = models.DateField(("Doctor last visited on"),default=None,blank=True)
    dateTime = models.DateTimeField(("Date Time"),default=now)
    
    pending = 'Pending'
    critical = 'Critical'
    recovering = 'Recovering'
    recovered = 'Recovered'
    deceased = 'Deceased'
    PATIENT_STATUS_CHOICES = [
        (pending,'pending'),
        (critical, 'critical'),
        (recovering, 'recovering'),
        (recovered, 'recovered'),
        (deceased, 'deceased'),]
        
    patientStatus = models.CharField(("Patient Status"),max_length=10,choices=PATIENT_STATUS_CHOICES,default=pending)

    def save(self, *args, **kwargs):
        cost = Bed.objects.filter(bedNumber = self.bedNumber ).update(occupied = True)
        
        super(Patient, self).save(*args, **kwargs)
        print(cost)
        

    def __str__(self):
        return self.patientName

class Symptoms(models.Model):
    symptomsId = models.AutoField(primary_key=True)
    symptoms = models.CharField(("Symptoms"),max_length=24,unique=True)
    active = models.BooleanField(("Active"))

    def __str__(self):
        return self.symptoms

class City(models.Model):
    cityId = models.AutoField(primary_key=True)
    stateName = models.ForeignKey('State',on_delete=models.CASCADE,null=True)
    cityName = models.CharField(("City Name"),max_length=24,unique=True)
    
    def __str__(self):
        return self.cityName

class PatientDocument(models.Model):
    patientName = models.ForeignKey('Patient',on_delete=models.CASCADE,null=True)
    document = models.FileField(("Document"))

    def __str__(self):
        return str(self.patientName) + "'s Document"

class PatientSymptom(models.Model):
    patientName = models.ForeignKey('Patient',on_delete=models.CASCADE,null=True)
    Symptoms = models.ForeignKey('Symptoms',on_delete=models.CASCADE,null=True,limit_choices_to={'active': True})

    def __str__(self):
        return str(self.patientName) + "'s Symptoms"

class Appointment(models.Model):
    appointmentId = models.AutoField(primary_key=True)
    caseNumber = models.IntegerField(('Case Number'),null=True,blank=True)
    patientName = models.CharField(("Patient Name"),max_length=24)
    patientEmail = models.EmailField(("Email Id"),unique=True)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone = models.IntegerField(("Phone Number"),validators=[validate_phoneNumber],unique=True)
    patientRelativeNumber = models.IntegerField(("Relative's Phone number"),validators=[validate_phoneNumber])
    patientRelativeName = models.CharField(("Relative's name"),max_length=24)
    reason = models.CharField(("Reason"),max_length=250)
    dateTime = models.DateTimeField(("Date Time"),default=now)

    def __str__(self):
        return self.patientName

class WardDoctor(models.Model):
    doctorName = models.ForeignKey('Doctor',on_delete=models.CASCADE,default=None,blank=True)
    wardName = models.ForeignKey('Ward',on_delete=models.CASCADE,default=None,blank=True)

    def __str__(self):
        return str(self.doctorName) +" - " + str(self.wardName)

class ContactUs(models.Model):
    contactId = models.AutoField(primary_key=True)
    contactName = models.CharField(("Name"),max_length=24,null=False)
    contactEmail = models.EmailField(("Email"),max_length=24,null=False)
    contactMsg = models.CharField(("Massage"),max_length=100)
    replyMsg = models.CharField(("Your Reply"),max_length=24,null=True)

    def __str__(self):
        return str(self.contactName) +" - " + str(self.contactEmail) +" - " + str(self.contactMsg)