from django.shortcuts import render
from django.http import HttpResponse
from .models import Film

def wszystkie_filmy(request):
    wszystkie = Film.objects.all    #syntax
    return render(request, "filmy.html", {'filmy': wszystkie}) #przekazanie obiektu w któym mamy tekst text



