from django.contrib import admin
from .models import *
# Register your models here.

class DocumentInline(admin.StackedInline):
    model = PatientDocument
    extra = 1

class SymptomInline(admin.StackedInline):
    model = PatientSymptom
    extra = 1


class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': [field.name for field in Patient._meta.get_fields() if field.name != "patientId" and field.name != "patientdoctor" and field.name != "patientdocument" and field.name != "patientsymptom"]}),
        
    ]
    inlines = [DocumentInline,SymptomInline]

class DoctorInline(admin.StackedInline):
    model = WardDoctor
    extra = 1

class WardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': [field.name for field in Ward._meta.get_fields() if field.name != "wardId" and field.name != "doctor" and field.name != "bed" and field.name != "warddoctor"]}),    
    ]
    inlines = [DoctorInline]

admin.site.register(Patient, PatientAdmin)
admin.site.register(City)
admin.site.register(State)
admin.site.register(PatientDocument)
admin.site.register(PatientSymptom)
admin.site.register(Symptoms)
admin.site.register(staff)
admin.site.register(Bed)
admin.site.register(Specialization)
admin.site.register(Doctor)
admin.site.register(Equipment)
admin.site.register(Oxygen)
admin.site.register(Ward,WardAdmin)
admin.site.register(Appointment)
admin.site.register(WardDoctor)