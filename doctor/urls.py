from django.urls import path
from .views import  patque,PatientRequest,prescribe,FindReport

urlpatterns = [
    path('doctor/',patque,name='doctor'),
    path('request/',PatientRequest,name='request'),
    path('prescribed/<int:pk>/',prescribe,name='prescribed'),
    path('search/',FindReport,name='search'),
]

