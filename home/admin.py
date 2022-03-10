from django.contrib import admin
from .models import *
# Register your models here.

perpage = 10
extrafield = 1

class CityAdmin(admin.ModelAdmin):
    list_per_page = perpage

class StateAdmin(admin.ModelAdmin):
    list_per_page = perpage

class PatientDocumentAdmin(admin.ModelAdmin):
    list_per_page = perpage

class PatientSymptomAdmin(admin.ModelAdmin):
    list_per_page = perpage

class SymptomsAdmin(admin.ModelAdmin):
    list_per_page = perpage

class staffAdmin(admin.ModelAdmin):
    list_per_page = perpage

class SpecializationAdmin(admin.ModelAdmin):
    list_per_page = perpage

class DoctorAdmin(admin.ModelAdmin):
    list_per_page = perpage

class EquipmentAdmin(admin.ModelAdmin):
    list_per_page = perpage

class OxygenAdmin(admin.ModelAdmin):
    list_per_page = perpage

class AppointmentAdmin(admin.ModelAdmin):
    list_per_page = perpage

class DocumentInline(admin.StackedInline):
    model = PatientDocument
    extra = extrafield

class SymptomInline(admin.StackedInline):
    model = PatientSymptom
    extra = extrafield

class BedAdmin(admin.ModelAdmin):
    list_per_page = perpage

class PatientAdmin(admin.ModelAdmin):
    list_per_page = perpage
    fieldsets = [
        (None,{'fields': [field.name for field in Patient._meta.get_fields() if field.name != "patientId" and field.name != "patientdoctor" and field.name != "patientdocument" and field.name != "patientsymptom"]}),
        
    ]
    inlines = [DocumentInline,SymptomInline]

class DoctorInline(admin.StackedInline):
    model = WardDoctor
    extra = extrafield

class WardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': [field.name for field in Ward._meta.get_fields() if field.name != "wardId" and field.name != "doctor" and field.name != "bed" and field.name != "warddoctor"]}),    
    ]
    inlines = [DoctorInline]
    list_display = ['wardName','wardPrice']

admin.site.register(Patient, PatientAdmin)
admin.site.register(City,CityAdmin)
admin.site.register(State,StateAdmin)
admin.site.register(PatientDocument,PatientDocumentAdmin)
admin.site.register(PatientSymptom,PatientSymptomAdmin)
admin.site.register(Symptoms,SymptomsAdmin)
admin.site.register(staff,staffAdmin)
admin.site.register(Bed,BedAdmin)
admin.site.register(Specialization,SpecializationAdmin)
admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Equipment,EquipmentAdmin)
admin.site.register(Oxygen,OxygenAdmin)
admin.site.register(Ward,WardAdmin)
admin.site.register(Appointment,AppointmentAdmin)