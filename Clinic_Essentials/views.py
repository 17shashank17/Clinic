from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Appointment,Feedback
# Create your views here.

def home(request):
    # return HttpResponse('Welcome')
    print("HI")
    return render(request,'Clinic_Essentials/home.html')

def appointment(request):
    print("Hi 1")
    if request.method=="POST":
        print("Hi 2")
        print(request.POST.get('patient_name'))
        obj=Appointment()
        obj.patient_name=request.POST.get('patient_name')
        obj.patient_number=request.POST.get('contact_number')
        obj.problem_detail=request.POST.get('problem_detail')
        obj.save()
        return render(request,'Clinic_Essentials/home.html',{'message':'Appointment Requested. Soon, Our doctor will contact you!'})
