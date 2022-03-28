from django.contrib import admin
from .models import *
from tinymce.widgets import TinyMCE
# Register your models here.

class PageAdmin(admin.ModelAdmin):

    formfield_overides = {
        models.TextField : {'widget':TinyMCE()},
    }

getdata = configuration.objects.all().values()
for i in getdata:
    if i['fieldname'] == 'perpage':
        perpage = i['value']
    if i['fieldname'] == 'extrafield':
        extrafield = i['value']
    if i['fieldname'] == 'maxfield':
        maxfield = i['value']

class configurationAdmin(admin.ModelAdmin):
    list_display = ['label','value']

class CityAdmin(admin.ModelAdmin):
    list_per_page = perpage
    list_display = ['stateName','cityName']

class StateAdmin(admin.ModelAdmin):
    list_per_page = perpage

class PatientDocumentAdmin(admin.ModelAdmin):
    list_per_page = perpage

class PatientSymptomAdmin(admin.ModelAdmin):
    list_per_page = perpage
    list_display = ['patientName','Symptoms']

class SymptomsAdmin(admin.ModelAdmin):
    list_per_page = perpage
    list_display = ['symptoms','active']

class staffAdmin(admin.ModelAdmin):
    list_per_page = perpage
    list_display = ['staffUserName','staffLastName','staffContactNumber','status']

class SpecializationAdmin(admin.ModelAdmin):
    list_per_page = perpage

class DoctorAdmin(admin.ModelAdmin):
    list_per_page = perpage
    list_display = ['doctorName','doctorUsername','doctorContact','Specialization']

class EquipmentAdmin(admin.ModelAdmin):
    list_per_page = perpage
    list_display = ['equipment_Name','equipment_Quantity','equipment_Assigned','equipment_Usable']

class OxygenAdmin(admin.ModelAdmin):
    list_per_page = perpage
    list_display = ['oxygen_Total_Hour','oxygen_Used','oxygen_Remaining','oxygen_Remaining_Hour']

class AppointmentAdmin(admin.ModelAdmin):
    list_per_page = perpage
    list_display = ['caseNumber','patientName','patientEmail','phone','patientRelativeNumber','reason','dateTime']

class DocumentInline(admin.StackedInline):
    model = PatientDocument
    extra = extrafield
    list_display = ['patientName','document']

class SymptomInline(admin.StackedInline):
    model = PatientSymptom
    extra = extrafield
    max_num = maxfield
    list_display = ['patientName','Symptoms']

class BedAdmin(admin.ModelAdmin):
    list_per_page = perpage
    list_display = ['wardName','bedNumber','occupied']

class PatientAdmin(admin.ModelAdmin):
    list_per_page = perpage
    fieldsets = [
        (None,{'fields': [field.name for field in Patient._meta.get_fields() if field.name != "patientId" and field.name != "patientdoctor" and field.name != "patientdocument" and field.name != "patientsymptom"]}),
        
    ]
    inlines = [DocumentInline,SymptomInline]
    list_display = ['caseNumber','patientName','phone','patientRelativeNumber','bedNumber','doctorName','doctorLastVisited']

class DoctorInline(admin.StackedInline):
    model = WardDoctor
    extra = extrafield
    max_num = maxfield
    list_display = ['doctorName','doctorUsername','doctorContact','Specialization']

class WardAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,{'fields': [field.name for field in Ward._meta.get_fields() if field.name != "wardId" and field.name != "doctor" and field.name != "bed" and field.name != "warddoctor" and field.name != "patient"]}),    
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
admin.site.register(configuration,configurationAdmin)
admin.site.register(page,PageAdmin)
admin.site.register(block)
admin.site.register(ContactUs)