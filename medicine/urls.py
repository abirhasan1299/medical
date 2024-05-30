from django.urls import path
from .views import add_med, autocompleteB,medview,presCrip,print,autocompleteG,PatList,PatData,Register,loginUser,logoutUser, userprofile, viewprofile

urlpatterns = [
    path('addmedicine/',add_med,name='Add Medicine'),
    path('viewmed/', medview, name='Medicine View'),
    path('prescription/', presCrip, name='Prescription'),
    path('print/', print, name='Print'),
    path('prescriptionG/',autocompleteG,name='group'),
    path('prescriptionB/',autocompleteB,name='Brand'),
    path('patient_list/',PatList,name='patient_list'),
   # path('patient_data/<int:pk>/',PatData.as_view(),name='patient_data'),
    path('register/', Register, name='register'),
    path('login/',loginUser,name='login'),
    path('logout/',logoutUser,name='logout'),
    path('plus_profile/',userprofile,name='plus_profile'),
    path('myprofile/',viewprofile,name='myprofile'),
]