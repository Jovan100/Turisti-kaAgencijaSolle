from django.contrib import admin
from korisnik.models import Korisnik

class KorisnikAdmin(admin.ModelAdmin):
    search_fields = ['ime', 'prezime', 'email']
    list_display = ['ime', 'prezime', 'email', 'broj_telefona']
    class Meta:
        model = Korisnik

admin.site.register(Korisnik, KorisnikAdmin)
