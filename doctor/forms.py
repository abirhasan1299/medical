
from django import forms
from .models import patientQuery

class PatientQuery(forms.ModelForm):
    class Meta:
        model = patientQuery
        fields = '__all__'
class prescripForm(forms.Form):
    
    TYPES = (
        ('Cap', 'Cap'),
        ('Syp', 'Syp'),
        ('Tab', 'Tab'),
        ('Sus', 'Sus'),
        ('Oral','Oral'),
        ('Injec','Injec'),
    )
    TIME = (
        ('1+1+1', '1+1+1'),
        ('1+0+1', '1+0+1'),
        ('1+0+0', '1+0+0'),
        ('0+1+1', '0+1+1'),
        ('0+1+0', '0+1+0'),
        ('0+0+1', '0+0+1'),
        ('1+1+0', '1+1+0'),
    )
    name = forms.CharField(max_length=100)
    gender = forms.CharField(max_length=10)
    mobile = forms.IntegerField()
    email = forms.EmailField()
    age = forms.CharField(max_length=10)
    date = forms.DateField(widget=forms.TextInput(
        attrs={'type': 'date'}))
    symptoms = forms.CharField(max_length=2000,widget=forms.Textarea)
    advice = forms.CharField(max_length=2000,required=False,widget=forms.Textarea)
    investigation = forms.CharField(
        max_length=2000, required=False, widget=forms.Textarea)
    disease = forms.CharField(max_length=2000)
    time = forms.TimeField(widget=forms.TextInput(attrs={'type':'time'}))
    #level-1
    med_types_1 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES),required=False)
    grp_1 = forms.CharField(
        max_length=1000,  required=False)
    taken_time_1 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_1 = forms.CharField(max_length=100, required=False)
    qty_1 = forms.CharField(max_length=100,required=False)
    #level-2
    med_types_2 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES),required=False)
    grp_2 = forms.CharField(
        max_length=1000,  required=False)
    taken_time_2 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_2 = forms.CharField(max_length=100, required=False)
    qty_2 = forms.CharField(max_length=100,required=False)
    #level-3
    med_types_3 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_3 = forms.CharField(
        max_length=1000,  required=False)
    taken_time_3 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_3 = forms.CharField(max_length=100, required=False)
    qty_3 = forms.CharField(max_length=100, required=False)

    #level-4
    med_types_4 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_4 = forms.CharField(
        max_length=1000,  required=False)
    taken_time_4 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_4 = forms.CharField(max_length=100, required=False)
    qty_4 = forms.CharField(max_length=100, required=False)
    #level-5
    med_types_5 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_5 = forms.CharField(
        max_length=1000,  required=False)
    taken_time_5 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_5 = forms.CharField(max_length=100, required=False)
    qty_5 = forms.CharField(max_length=100, required=False)
    #level-6
    med_types_6 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_6 = forms.CharField(
        max_length=1000,  required=False)
    taken_time_6 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_6 = forms.CharField(max_length=100, required=False)
    qty_6 = forms.CharField(max_length=100, required=False)
    #level-7
    med_types_7 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_7 = forms.CharField(
        max_length=1000,  required=False)
    taken_time7 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_7 = forms.CharField(max_length=100, required=False)
    qty_7= forms.CharField(max_length=100, required=False)
    #level-8
    med_types_8 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_8 = forms.CharField(
        max_length=1000,  required=False)
    taken_time8 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_8= forms.CharField(max_length=100, required=False)
    qty_8= forms.CharField(max_length=100, required=False)
    #level-9
    med_types_9 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_9 = forms.CharField(
        max_length=1000,  required=False)
    taken_time9 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_9= forms.CharField(max_length=100, required=False)
    qty_9= forms.CharField(max_length=100, required=False)
    #level-10
    med_types_10 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_10 = forms.CharField(
        max_length=1000,  required=False)
    taken_time10 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_10= forms.CharField(max_length=100, required=False)
    qty_10= forms.CharField(max_length=100, required=False)
    #level-11
    med_types_11 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_11 = forms.CharField(
        max_length=1000,  required=False)
    taken_time11 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_11= forms.CharField(max_length=100, required=False)
    qty_11= forms.CharField(max_length=100, required=False)
    #level-12
    med_types_12 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_12 = forms.CharField(
        max_length=1000,  required=False)
    taken_time12 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_12= forms.CharField(max_length=100, required=False)
    qty_12= forms.CharField(max_length=100, required=False)
    #level-13
    med_types_13 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_13 = forms.CharField(
        max_length=1000,  required=False)
    taken_time13 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_13= forms.CharField(max_length=100, required=False)
    qty_13= forms.CharField(max_length=100, required=False)
    #level-14
    med_types_14 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_14 = forms.CharField(
        max_length=1000,  required=False)
    taken_time14 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_14= forms.CharField(max_length=100, required=False)
    qty_14= forms.CharField(max_length=100, required=False)
    #level-15
    med_types_15 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_15 = forms.CharField(
        max_length=1000,  required=False)
    taken_time15 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_15= forms.CharField(max_length=100, required=False)
    qty_15= forms.CharField(max_length=100, required=False)
    #level-16
    med_types_16 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_16 = forms.CharField(
        max_length=1000,  required=False)
    taken_time16 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_16= forms.CharField(max_length=100, required=False)
    qty_16= forms.CharField(max_length=100, required=False)
    #level-17
    med_types_17 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_17 = forms.CharField(
        max_length=1000,  required=False)
    taken_time17 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_17= forms.CharField(max_length=100, required=False)
    qty_17= forms.CharField(max_length=100, required=False)
    #level-18
    med_types_108= forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_18 = forms.CharField(
        max_length=1000,  required=False)
    taken_time18 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_18= forms.CharField(max_length=100, required=False)
    qty_18= forms.CharField(max_length=100, required=False)
    #level-19
    med_types_19 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_19 = forms.CharField(
        max_length=1000,  required=False)
    taken_time19 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_19= forms.CharField(max_length=100, required=False)
    qty_19= forms.CharField(max_length=100, required=False)
    #level-20
    med_types_20 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TYPES), required=False)
    grp_20 = forms.CharField(
        max_length=1000,  required=False)
    taken_time20 = forms.CharField(
        max_length=100, widget=forms.Select(choices=TIME), required=False)
    day_20= forms.CharField(max_length=100, required=False)
    qty_20= forms.CharField(max_length=100, required=False)