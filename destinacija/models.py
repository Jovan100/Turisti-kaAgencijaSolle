from django.db import models

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

    def __str__(slef):
        return self.naziv

    class Meta:
        verbose_name_plural = "Agencije"

class Destinacija(models.Model):
    naziv = models.CharField(max_length=100, unique=True)
    zemlja = models.ForeignKey(Zemlja, on_delete=models.CASCADE)
    kategorija = models.ForeignKey(KategorijaDestinacije, on_delete=models.CASCADE)
    opis = models.TextField(null=True, blank=True)
    preporuka = models.BooleanField(default=False)
    slika = models.ImageField(upload_to='slike', blank=True, null=True)

    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name_plural = "Destinacije"
