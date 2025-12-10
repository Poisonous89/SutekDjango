from django.db import models

class Osoba(models.Model):
    meno = models.CharField(max_length=100)
    priezvisko = models.CharField(max_length=100)
    vek = models.IntegerField()
    datum = models.DateField()
    email = models.EmailField()
    muz = models.BooleanField()

    def __str__(self):
        return f"{self.meno} {self.priezvisko}"


class Student(models.Model):
    meno = models.CharField(max_length=100)
    priezvisko = models.CharField(max_length=100)
    trieda = models.CharField(max_length=10)
    vek = models.IntegerField()
    muz = models.BooleanField()

    def __str__(self):
        return f"{self.meno} {self.priezvisko} {self.trieda}"