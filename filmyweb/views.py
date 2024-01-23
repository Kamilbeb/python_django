from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Film
from .forms import FilmForm

def wszystkie_filmy(request):
    wszystkie = Film.objects.all()    #syntax
    return render(request, "filmy.html", {'filmy': wszystkie}) #przekazanie obiektu w któym mamy tekst text

def nowy_film(request): #funkcja która przeforamtuje formularz i wyśle dane do dazy danych
    #przypisujemy dane które przychodzą przez request do zmiennej form
    form = FilmForm(request.POST or None, request.FILES or None) #to jest nazwa klasy którą stworzyliśmy w forms i
                                                                # musimy to zaimportować
    if form.is_valid(): #sprawdzamy czy ten form spełnia wymagania które określiliśmy
        form.save() #jeżeli spełnia wymagania to robimy save
        return redirect(wszystkie_filmy)  # funkcja odsyła nas do wszystkich filmów

    return render(request, 'film_form.html', {'form': form})

def edytuj_film(request, id):
    film = get_object_or_404(Film, pk=id) # jako pierwszy parametr model a drugi pk czyli primary key
    form = FilmForm(request.POST or None, request.FILES or None, instance=film) #dodatkowy instance parametr do którego przesyłamy film

    if form.is_valid():
        form.save()
        return redirect(wszystkie_filmy) #funkcja odsyła nas do wszystkich filmów

    return render(request, 'film_form.html', {'form': form})
