from django.shortcuts import render,HttpResponse
from doctor.models import patientQuery


def home(request):
    data = patientQuery.objects.all().order_by('-id')[0:10]
    
    context={
        'data':data
    }
    return render(request,'basic.html',context)

def about(request):
    return render(request,'about.html')