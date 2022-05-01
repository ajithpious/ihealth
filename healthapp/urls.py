from .views import getpulse, getspo2, gettemp, home, patient, patients
from django.urls import path


urlpatterns = [ path('',home),
path("patients",patients),
path("patient1",patient),
path("temp",gettemp),
path("pulse",getpulse),
path("spo2",getspo2)
]