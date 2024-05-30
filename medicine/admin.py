from django.contrib import admin
from .models import AddMedicine,PatientData, UserProfile


# Register your models here.


admin.site.register(AddMedicine)
admin.site.register(PatientData)
admin.site.register(UserProfile)