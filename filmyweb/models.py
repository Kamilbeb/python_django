from django.db import models

class Film(models.Model):   #tworzymy klasę która nazywa się jak encja w bazie danych i
                                # chcemy żeby miała wszystkie metody z klasy Model
    tytul = models.CharField(max_length=64, blank=False, unique=True)
                                                            #CharField odpowiada za przechowywanie danych tekstowych
                                                            #blank=False oznacza że pole nazwa nie może być puste - wymagane
    rok = models.PositiveIntegerField(default=2000)
    opis = models.TextField(default="")
    premiera = models.DateField(null=True, blank=True)
    imdb_rating = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)   #ranking imdb
    plakat = models.ImageField(upload_to="plakaty", null=True, blank=True) #gdzie będą upload nasze zdjęcia

    def __str__(self):  #jak chcemy żeby dany rekord z bazy wyświetlić jako string
        return self.tytul_z_rokiem()

    def tytul_z_rokiem(self):
        return "{} ({})".format(self.tytul, self.rok)





