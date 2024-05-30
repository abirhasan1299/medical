from django.contrib import admin
from .models import patientQuery,Prescription

# Register your models here

admin.site.register(patientQuery)
admin.site.register(Prescription)
