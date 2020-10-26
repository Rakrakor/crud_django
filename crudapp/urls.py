from django.contrib import admin
from django.urls import path, include
from crudapp import views
from crudapp.views import Airportlist

urlpatterns = [
     path('airportform/', views.airportform, name='newairport'),
     path('airportlist/', Airportlist.as_view(), name='airportlist'),
     path('updateairportdetails/<int:id>', views.updateairportdetails, name='updateairportdetails'),
     path('deleteairport/<int:id>', views.deleteairport, name='deleteairport'),
]

