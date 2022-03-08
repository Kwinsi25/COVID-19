from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('bedAvailablity/',views.bedAvailablity,name = 'bedAvailablity'),
    path('staffDashboard/',views.staffDashboard,name='staffDashboard'),
    path('doctorDashboard/',views.doctorDashboard,name='doctorDashboard'),
    path('index/',views.home,name='index'),
    path('patient/',views.patient,name="patient"),
    path('bookAppointment/',views.bookAppointment,name='bookAppointment'),
    path('viewPatient/',views.viewPatient,name="viewPatient"),
    path('getbedsajax/', views.getbedsajax, name="getbedsajax"),
]
