from django.contrib import admin
from korisnik.models import Korisnik
from django.contrib.auth.models import Group

class KorisnikAdmin(admin.ModelAdmin):
    search_fields = ['ime', 'prezime', 'email']
    list_display = ['ime', 'prezime', 'email', 'broj_telefona']
    class Meta:
        model = Korisnik

admin.site.register(Korisnik, KorisnikAdmin)
admin.site.unregister(Group)
