from .views import getdata, home, patient, patients
from django.urls import path


urlpatterns = [ path('',home),
path("patients",patients),
path("patient1",patient),
path("getdata",getdata)
]