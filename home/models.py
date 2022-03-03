
from django.db import models

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
         
class Bed(models.Model):
    bedId = models.AutoField(primary_key=True,max_length=24)
    bedNumber = models.CharField(max_length=5)
    occupied = models.BooleanField(default=False)

    def __str__(self):
        return str(self.bedNumber)

class Specialization(models.Model):
    specializationId = models.AutoField(primary_key=True)
    specialization = models.CharField(max_length=64)

    def __str__(self):
        return self.specialization

class Doctor(models.Model):
    doctorId = models.AutoField(primary_key=True)
    doctorName = models.CharField(max_length=24)
    doctorUsername=models.CharField(max_length=15)
    doctorPass=models.CharField(max_length=100)
    doctorContact = models.IntegerField()
    specialization = models.ForeignKey('Specialization',on_delete = models.CASCADE,null=False)

    def __str__(self):
        return self.doctorName