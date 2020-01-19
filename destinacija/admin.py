from django.contrib import admin
from destinacija.models import (
    Agencija,
    Cenovnik,
    Destinacija,
    KategorijaDestinacije,
    Regija,
    Zemlja
)

class AgencijaAdmin(admin.ModelAdmin):
    search_fields = ['naziv']
    list_display = ['naziv']
    class Meta:
        model = Agencija

class CenovnikAdmin(admin.ModelAdmin):
    search_fields = ['naziv']
    list_display = ['naziv', 'destinacija', 'agencija', 'broj_nocenja', 'polasci', 'fajl']
    class Meta:
        model = Cenovnik

class DestinacijaAdmin(admin.ModelAdmin):
    search_fields = ['naziv']
    list_display = ['naziv', 'zemlja', 'kategorija', 'preporuka', 'regija', 'slika']
    list_filter = ['preporuka']
    class Meta:
        model = Destinacija

class KategorijaDestinacijeAdmin(admin.ModelAdmin):
    search_fields = ['naziv']
    list_display = ['naziv', 'slika']
    class Meta:
        model = KategorijaDestinacije

class RegijaAdmin(admin.ModelAdmin):
    search_fields = ['naziv']
    list_display = ['naziv']
    class Meta:
        model = Regija


class ZemljaAdmin(admin.ModelAdmin):
    search_fields = ['naziv']
    list_display = ['naziv', 'slika']
    class Meta:
        model = Zemlja

admin.site.register(Agencija, AgencijaAdmin)
admin.site.register(Cenovnik, CenovnikAdmin)
admin.site.register(Destinacija, DestinacijaAdmin)
admin.site.register(KategorijaDestinacije, KategorijaDestinacijeAdmin)
admin.site.register(Regija, RegijaAdmin)
admin.site.register(Zemlja, ZemljaAdmin)
