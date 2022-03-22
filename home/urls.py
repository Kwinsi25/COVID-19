from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('bedAvailablity/',views.bedAvailablity,name = 'bedAvailablity'),
    path('staffDashboard/',views.staffDashboard,name='staffDashboard'),
    path('doctorDashboard/',views.doctorDashboard,name='doctorDashboard'),
    path('/',views.home,name='index'),
    path('patient/',views.patient,name="patient"),
    path('bookAppointment/',views.bookAppointment,name='bookAppointment'),
    path('bookAppointment/bookedAppointment',views.bookedAppointment,name='bookedAppointment'),
    path('viewPatient/',views.viewPatient,name="viewPatient"),
    path('getbedsajax/', views.getbedsajax, name="getbedsajax"),
    path('getdoctorsajax/', views.getdoctorsajax, name="getdoctorsajax"),
    path('getcitiesajax/', views.getcitiesajax, name="getcitiesajax"),
    path('getpricesajax/', views.getpricesajax, name="getpricesajax"),
    path('email/', views.email, name="email"),
    path('message/',views.message,name="message"),
    path('confirmationDetails/',views.confirmationDetails,name="confirmationDetails"),
    path('confirmationDetails/confirmDetails/',views.confirmDetails,name='confirmDetails'),
    path('patient/confirmDetails/',views.confirmDetails,name='confirmDetails'),
    path('updatePatient/',views.updatePatient,name='updatePatient'),
    path('deletePatient/',views.deletePatient,name='deletePatient'),
    path('deleteAppointment/',views.deleteAppointment,name='deleteAppointment'),
    path('allPatientDoc.html/',views.allPatientDoc,name="allPatientDoc"),
    path('logout/',views.logout,name="logout"),

]
