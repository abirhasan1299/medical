from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render,redirect
from .forms import PatientQuery,prescripForm
from .models import patientQuery,Prescription
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from notifications.signals import notify
#from django.views.generic import DetailView


def  FindReport(request):
    query = request.GET['email']
    post = Prescription.objects.filter(email__icontains=query)
    context={
        'post':post
    }
    return render(request,'doctor/findreport.html',context)

@login_required
def PatientRequest(request):
    data = patientQuery.objects.all().order_by('-id')
    pres = Prescription.objects.all().order_by('-id')[0:1]
    context={
        'data':data,
        'pres':pres
    }
    return render(request, 'doctor/request.html', context)

def patque(request):
    if request.method == 'POST':
        form = PatientQuery(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'* Your Problem Send to Doctor... *')
            return redirect('home')
    else:
        form = PatientQuery()
    context={
        'form':form
    }
    return render(request,'doctor/doctor.html',context)

@login_required
def prescribe(request,pk):
    post = patientQuery.objects.all().get(id=pk)
    
    if request.method == 'POST':
        form = prescripForm(request.POST)
        if form.is_valid():
                    name = request.POST['name']
                    gender = request.POST['gender']
                    age = request.POST['age']
                    date = request.POST['date']
                    symptoms = request.POST['symptoms']
                    disease = request.POST['disease']
                    time = request.POST['time']
                    investigation = request.POST['investigation']
                    advice = request.POST['advice']
                    mobile = request.POST['mobile']
                
                    #level-1
                    med_types_1 = request.POST['med_types_1']
                    grp_1 = request.POST['grp_1']
                
                    taken_time_1 = request.POST['taken_time_1']
                    qty_1 = request.POST['qty_1']
                    day_1 = request.POST['day_1']
                    #level-2
                    med_types_2 = request.POST['med_types_2']
                    grp_2 = request.POST['grp_2']
                    
                    taken_time_2 = request.POST['taken_time_2']
                    qty_2 = request.POST['qty_2']
                    day_2 = request.POST['day_2']
                    #level-3
                    med_types_3 = request.POST['med_types_3']
                    grp_3 = request.POST['grp_3']
                    
                    taken_time_3 = request.POST['taken_time_3']
                    qty_3 = request.POST['qty_3']
                    day_3 = request.POST['day_3']
                    #level-4
                    med_types_4 = request.POST['med_types_4']
                    grp_4 = request.POST['grp_4']
                    
                    taken_time_4 = request.POST['taken_time_4']
                    qty_4 = request.POST['qty_4']
                    day_4 = request.POST['day_4']
                    #level-5
                    med_types_5 = request.POST['med_types_5']
                    grp_5 = request.POST['grp_5']
                    
                    taken_time_5 = request.POST['taken_time_5']
                    qty_5 = request.POST['qty_5']
                    day_5 = request.POST['day_5']
                    #level-6
                    med_types_6 = request.POST['med_types_6']
                    grp_6 = request.POST['grp_6']
                    
                    taken_time_6 = request.POST['taken_time_6']
                    qty_6 = request.POST['qty_6']
                    day_6 = request.POST['day_6']
                    #level-7
                    med_types_7 = request.POST['med_types_7']
                    grp_7 = request.POST['grp_7']
                    
                    taken_time_7 = request.POST['taken_time_7']
                    qty_7 = request.POST['qty_7']
                    day_7 = request.POST['day_7']
                    #level-8
                    med_types_8 = request.POST['med_types_8']
                    grp_8 = request.POST['grp_8']
                    
                    taken_time_8 = request.POST['taken_time_8']
                    qty_8 = request.POST['qty_8']
                    day_8 = request.POST['day_8']
                    #level-9
                    med_types_9 = request.POST['med_types_9']
                    grp_9 = request.POST['grp_9']
                
                    taken_time_9 = request.POST['taken_time_9']
                    qty_9 = request.POST['qty_9']
                    day_9 = request.POST['day_9']
                    #level-10
                    med_types_10 = request.POST['med_types_10']
                    grp_10 = request.POST['grp_10']
                    
                    taken_time_10 = request.POST['taken_time_10']
                    qty_10 = request.POST['qty_10']
                    day_10 = request.POST['day_10']
                    #level-11
                    med_types_11 = request.POST['med_types_11']
                    grp_11 = request.POST['grp_11']
                    
                    taken_time_11 = request.POST['taken_time_11']
                    qty_11 = request.POST['qty_11']
                    day_11 = request.POST['day_11']
                    #level-12
                    med_types_12 = request.POST['med_types_12']
                    grp_12 = request.POST['grp_12']
                
                    taken_time_12 = request.POST['taken_time_12']
                    qty_12 = request.POST['qty_12']
                    day_12 = request.POST['day_12']
                    
                    #level-13
                    med_types_13 = request.POST['med_types_13']
                    grp_13 = request.POST['grp_13']
                
                    taken_time_13 = request.POST['taken_time_13']
                    qty_13 = request.POST['qty_13']
                    day_13 = request.POST['day_13']
                    #level-14
                    med_types_14 = request.POST['med_types_14']
                    grp_14 = request.POST['grp_14']
                    
                    taken_time_14 = request.POST['taken_time_14']
                    qty_14 = request.POST['qty_14']
                    day_14 = request.POST['day_14']
                    #level-15
                    med_types_15 = request.POST['med_types_15']
                    grp_15 = request.POST['grp_15']
                
                    taken_time_15 = request.POST['taken_time_15']
                    qty_15 = request.POST['qty_15']
                    day_15 = request.POST['day_15']
                    #level-16
                    med_types_16 = request.POST['med_types_16']
                    grp_16 = request.POST['grp_16']
                    
                    taken_time_16 = request.POST['taken_time_16']
                    qty_16 = request.POST['qty_16']
                    day_16 = request.POST['day_16']
                    #level-17
                    med_types_17 = request.POST['med_types_17']
                    grp_17 = request.POST['grp_17']
                    
                    taken_time_17 = request.POST['taken_time_17']
                    qty_17 = request.POST['qty_17']
                    day_17 = request.POST['day_17']
                    #level-18
                    med_types_18 = request.POST['med_types_18']
                    grp_18 = request.POST['grp_18']
                    email = request.POST['email']
                    taken_time_18 = request.POST['taken_time_18']
                    qty_18 = request.POST['qty_18']
                    day_18 = request.POST['day_18']
                    #level-19
                    med_types_19 = request.POST['med_types_19']
                    grp_19 = request.POST['grp_19']
                
                    taken_time_19 = request.POST['taken_time_19']
                    qty_19 = request.POST['qty_19']
                    day_19 = request.POST['day_19']
                    #level-20
                    med_types_20 = request.POST['med_types_20']
                    grp_20 = request.POST['grp_20']
                    taken_time_20 = request.POST['taken_time_20']
                    qty_20 = request.POST['qty_20']
                    day_20 = request.POST['day_20']

                    object = Prescription(name=name, age=age, date=date, symptoms=symptoms,
                                    disease=disease, time=time, med_types_1=med_types_1, med_types_2=med_types_2, med_types_3=med_types_3, med_types_4=med_types_4, med_types_5=med_types_5, med_types_6=med_types_6, med_types_7=med_types_7,med_types_8=med_types_8,med_types_9=med_types_9,med_types_10=med_types_10,med_types_11=med_types_11,med_types_12=med_types_12,med_types_13=med_types_13,med_types_14=med_types_14,med_types_15=med_types_15,med_types_16=med_types_16,med_types_17=med_types_17,med_types_18=med_types_18,med_types_19=med_types_19,med_types_20=med_types_20, grp_1=grp_1, grp_2=grp_2, grp_3=grp_3, grp_4=grp_4, grp_5=grp_5, grp_6=grp_6, grp_7=grp_7,grp_8=grp_8,grp_9=grp_9,grp_10=grp_10,grp_11=grp_11,grp_12=grp_12,grp_13=grp_13,grp_14=grp_14,grp_15=grp_15,grp_16=grp_16,grp_17=grp_17,grp_18=grp_18,grp_19=grp_19,grp_20=grp_20, taken_time_1=taken_time_1, taken_time_2=taken_time_2, taken_time_3=taken_time_3, taken_time_4=taken_time_4, taken_time_5=taken_time_5, taken_time_6=taken_time_6, taken_time_7=taken_time_7,taken_time_8=taken_time_8,taken_time_9=taken_time_9,taken_time_10=taken_time_10,taken_time_11=taken_time_11,email=email,taken_time_12=taken_time_12,taken_time_13=taken_time_13,taken_time_14=taken_time_14,taken_time_15=taken_time_15,taken_time_16=taken_time_16,taken_time_17=taken_time_17,taken_time_18=taken_time_18,taken_time_19=taken_time_19,taken_time_20=taken_time_20, qty_1=qty_1, qty_2=qty_2, qty_3=qty_3, qty_4=qty_4, qty_5=qty_5, qty_6=qty_6, qty_7=qty_7, day_5=day_5, day_4=day_4, day_3=day_3, day_2=day_2, day_1=day_1, day_6=day_6, day_7=day_7,day_8=day_8,day_9=day_9,day_10=day_10,day_11=day_11,day_12=day_12,day_13=day_13,day_14=day_14,day_15=day_15,day_16=day_16,day_17=day_17,day_18=day_18,day_19=day_19,day_20=day_20,qty_8=qty_8,qty_9=qty_9,qty_10=qty_10,qty_11=qty_11,qty_12=qty_12,qty_13=qty_13,qty_14=qty_14,qty_15=qty_15,qty_16=qty_16,qty_17=qty_17,qty_18=qty_18,qty_19=qty_19,qty_20=qty_20, investigation=investigation, advice=advice,mobile=mobile,gender=gender)
                    object.save()
                    post.delete()
                    messages.success(request,'CheckUp Done..*')
                    return redirect('request')
    else:
        form = prescripForm()
    context = {
                    'form':form,
                    'range':range(1,21),
                    'pk':post,
            }
    return render(request,'doctor/sheet.html',context)
