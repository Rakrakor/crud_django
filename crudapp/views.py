from django.shortcuts import render, redirect
from crudapp.forms import AirportForm
from crudapp.models import Airport
from django.views.generic import ListView
from django.contrib import messages

from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

#CREATE: add a new airport
def airportform(request):
    if request.method == "POST":
        form = AirportForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'The airport form is complete')
            return redirect('/airportlist/')
    else:
        form = AirportForm()
    return render(request, 'crudapp/airportForm.html', {'form': form})

#READ: List all objects contained in Airportlist
# returns all Airport object to the template via object_list or
# under the specified named list
class Airportlist(ListView):
    model = Airport
    context_object_name = 'airport_object_list'

#UPDATE: an existing airport
#NOTE:.get() returns an individual object and .update() only works on querysets,
# such as what would be returned with .filter() instead of .get().
def updateairportdetails(request, id):
    form = AirportForm(request.POST)
    if request.method == "POST":
        form = AirportForm(request.POST)
        if form.is_valid():
            Airport.objects.filter(pk=id).update(city=request.POST['city'], airport=request.POST['airport'], acronym=request.POST['acronym'])
            return redirect('/airportlist/')
    else:
        #Pre-fill form with existing object attributes
        airport = Airport.objects.get(pk=id)
        data = {'acronym': airport.acronym, 'airport': airport.airport, 'city': airport.city}
        form = AirportForm(initial=data)
    return render(request, 'crudapp/airportForm.html', {'form': form})


#DELETE
def deleteairport(request, id):
    airportselected = Airport.objects.get(pk=id)
    airportselected.delete()

    return redirect('/airportlist/')






