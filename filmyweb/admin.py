from django.contrib import admin
from .models import Film    #musimy zaimportować folder projektu

#admin.site.register(Film)   #rejestrujemy projekt Film

@admin.register(Film)   #inny sposób rejestracji dzięki temu w klasie możemy dodawać różne opcje
class FilmAdmin(admin.ModelAdmin):
    #fields = ["tytul", "opis", "rok"]
    #exclude = ["opis"]  #jeżeli chcemy włączyć wszystkie poza opisem
    list_display = ["tytul", "imdb_rating", "rok"] #kolejny sposób
    list_filter = ("rok", "imdb_rating")
    search_fields = ("tytul", "opis")