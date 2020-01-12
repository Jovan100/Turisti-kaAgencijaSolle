from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from korisnik.managers import KorisnikManager

class Korisnik(AbstractBaseUser):
    ime = models.CharField(max_length=100)
    prezime = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    broj_telefona = models.CharField(max_length=100)
    username = models.CharField(max_length=255, unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['ime', 'prezime', 'email', 'broj_telefona']

    objects = KorisnikManager()

    def __str__(self):
        return self.ime + ' ' + self.prezime

    def get_full_name(self):
        return self.ime + ' ' + self.prezime

    def get_short_name(self):
        return self.ime

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    class Meta:
        verbose_name_plural = "Korisnici"
