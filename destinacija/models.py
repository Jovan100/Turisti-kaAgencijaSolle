from django.db import models
from destinacija.validators import validate_file_extension

class Zemlja(models.Model):
    naziv = models.CharField(max_length=100, unique=True)
    slika = models.ImageField(upload_to='slike', blank=True, null=True)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name_plural = "Zemlje"

class KategorijaDestinacije(models.Model):
    naziv = models.CharField(max_length=100, unique=True)
    slika = models.ImageField(upload_to='slike', blank=True, null=True)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name_plural = "Kategorije Destinacija"

class Agencija(models.Model):
    naziv = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name_plural = "Agencije"

class Regija(models.Model):
    naziv = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name_plural = "Regije"

class Destinacija(models.Model):
    naziv = models.CharField(max_length=100, unique=True)
    zemlja = models.ForeignKey(Zemlja, on_delete=models.CASCADE)
    kategorija = models.ForeignKey(KategorijaDestinacije, on_delete=models.CASCADE)
    regija = models.ForeignKey(Regija, on_delete=models.SET_NULL, null=True)
    opis = models.TextField(null=True, blank=True)
    preporuka = models.BooleanField(default=False)
    slika = models.ImageField(upload_to='slike', blank=True, null=True)
    mapa = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name_plural = "Destinacije"


class Cenovnik(models.Model):
    naziv = models.CharField(max_length=100, unique=True)
    destinacija = models.ForeignKey(Destinacija, on_delete=models.CASCADE)
    agencija = models.ForeignKey(Agencija, on_delete=models.CASCADE)
    broj_nocenja = models.CharField(max_length=100)
    polasci = models.CharField(max_length=100, blank=True, null=True)
    fajl = models.FileField(upload_to='cenovnici', validators=[validate_file_extension])

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name_plural = "Cenovnici"
