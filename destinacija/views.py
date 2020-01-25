from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.views import View
from destinacija.models import (
    Agencija,
    Cenovnik,
    Destinacija,
    Regija,
    KategorijaDestinacije,
    Zemlja
)
from django.views.generic import (
    DetailView,
    ListView,
)

class PocetnaStranaView(TemplateView):
    template_name = 'destinacija/pocetna_strana.html'

class UsloviPutovanjaView(TemplateView):
    template_name = 'destinacija/opsti_uslovi_putovanja.html'

class TuristickiPojmoviView(TemplateView):
    template_name = 'destinacija/turisticki_pojmovi.html'

class PutnoOsiguranjeView(TemplateView):
    template_name = 'destinacija/putno_osiguranje.html'

class AvioKarteView(TemplateView):
    template_name = 'destinacija/avio_karte.html'

class ONamaView(TemplateView):
    template_name = 'destinacija/o_nama.html'

class KontaktView(TemplateView):
    template_name = 'destinacija/kontakt.html'

class GrckaListView(View):
    def get(self, request, *args, **kwargs):
        zemlja = Zemlja.objects.get(naziv="Grčka")
        kopno = KategorijaDestinacije.objects.get(naziv="Kopno")
        ostrvo = KategorijaDestinacije.objects.get(naziv="Ostrva")
        orfanska = Regija.objects.get(naziv="Orfanski zaliv")
        egej = Regija.objects.get(naziv="Egejska regija")
        jonska = Regija.objects.get(naziv="Jonska regija")
        olimpska = Regija.objects.get(naziv="Olimpska regija")
        atos = Regija.objects.get(naziv="Atos - treći prst")
        sitonija = Regija.objects.get(naziv="Sitonija - drugi prst")
        kasandra = Regija.objects.get(naziv="Kasandra - prvi prst")
        kopno_orfanska = Destinacija.objects.filter(zemlja=zemlja, kategorija=kopno, regija=orfanska)
        kopno_egej = Destinacija.objects.filter(zemlja=zemlja, kategorija=kopno, regija=egej)
        kopno_jonska = Destinacija.objects.filter(zemlja=zemlja, kategorija=kopno, regija=jonska)
        kopno_olimpska = Destinacija.objects.filter(zemlja=zemlja, kategorija=kopno, regija=olimpska)
        kopno_atos = Destinacija.objects.filter(zemlja=zemlja, kategorija=kopno, regija=atos)
        kopno_sitonija = Destinacija.objects.filter(zemlja=zemlja, kategorija=kopno, regija=sitonija)
        kopno_kasandra = Destinacija.objects.filter(zemlja=zemlja, kategorija=kopno, regija=kasandra)
        ostrva_egej = Destinacija.objects.filter(zemlja=zemlja, kategorija=ostrvo, regija=egej)
        ostrva_jonska = Destinacija.objects.filter(zemlja=zemlja, kategorija=ostrvo, regija=jonska)
        return render(request, 'destinacija/grcka.html',
            {
            'kopno_orfanska': kopno_orfanska,
            'kopno_egej': kopno_egej,
            'kopno_jonska': kopno_jonska,
            'kopno_olimpska': kopno_olimpska,
            'kopno_atos': kopno_atos,
            'kopno_sitonija': kopno_sitonija,
            'kopno_kasandra': kopno_kasandra,
            'ostrva_egej': ostrva_egej,
            'ostrva_jonska': ostrva_jonska,
            })

class GrckaKopnoView(View):
    def get(self, request, *args, **kwargs):
        zemlja = Zemlja.objects.get(naziv="Grčka")
        kopno = KategorijaDestinacije.objects.get(naziv="Kopno")
        orfanska = Regija.objects.get(naziv="Orfanski zaliv")
        egej = Regija.objects.get(naziv="Egejska regija")
        jonska = Regija.objects.get(naziv="Jonska regija")
        olimpska = Regija.objects.get(naziv="Olimpska regija")
        atos = Regija.objects.get(naziv="Atos - treći prst")
        sitonija = Regija.objects.get(naziv="Sitonija - drugi prst")
        kasandra = Regija.objects.get(naziv="Kasandra - prvi prst")
        kopno_orfanska = Destinacija.objects.filter(zemlja=zemlja, kategorija=kopno, regija=orfanska)
        kopno_egej = Destinacija.objects.filter(zemlja=zemlja, kategorija=kopno, regija=egej)
        kopno_jonska = Destinacija.objects.filter(zemlja=zemlja, kategorija=kopno, regija=jonska)
        kopno_olimpska = Destinacija.objects.filter(zemlja=zemlja, kategorija=kopno, regija=olimpska)
        kopno_atos = Destinacija.objects.filter(zemlja=zemlja, kategorija=kopno, regija=atos)
        kopno_sitonija = Destinacija.objects.filter(zemlja=zemlja, kategorija=kopno, regija=sitonija)
        kopno_kasandra = Destinacija.objects.filter(zemlja=zemlja, kategorija=kopno, regija=kasandra)
        return render(request, 'destinacija/kopno.html',
            {
            'kopno_orfanska': kopno_orfanska,
            'kopno_egej': kopno_egej,
            'kopno_jonska': kopno_jonska,
            'kopno_olimpska': kopno_olimpska,
            'kopno_atos': kopno_atos,
            'kopno_sitonija': kopno_sitonija,
            'kopno_kasandra': kopno_kasandra
            })

class GrckaOstrvaView(View):
    def get(self, request, *args, **kwargs):
        zemlja = Zemlja.objects.get(naziv="Grčka")
        ostrvo = KategorijaDestinacije.objects.get(naziv="Ostrva")
        egej = Regija.objects.get(naziv="Egejska regija")
        jonska = Regija.objects.get(naziv="Jonska regija")
        ostrva_egej = Destinacija.objects.filter(zemlja=zemlja, kategorija=ostrvo, regija=egej)
        ostrva_jonska = Destinacija.objects.filter(zemlja=zemlja, kategorija=ostrvo, regija=jonska)
        return render(request, 'destinacija/ostrva.html',
            {
            'ostrva_egej': ostrva_egej,
            'ostrva_jonska': ostrva_jonska,
            })

class DestinacijaView(View):
    def get(self, request, naziv_destinacije):
        destinacija = Destinacija.objects.get(naziv=naziv_destinacije)
        cenovnici = Cenovnik.objects.filter(destinacija=destinacija.id)
        return render(request, 'destinacija/destinacija.html',
            {
            'destinacija': destinacija,
            'cenovnici': cenovnici
            })

class LetoView(TemplateView):
    template_name = 'destinacija/leto.html'

class LetoZemljaView(View):
    def get(self, request, zemlja):
        zemlja_id = Zemlja.objects.get(naziv=zemlja)
        kopno = KategorijaDestinacije.objects.get(naziv="Kopno")
        ostrvo = KategorijaDestinacije.objects.get(naziv="Ostrva")
        destinacije_kopno = Destinacija.objects.filter(zemlja=zemlja_id, kategorija=kopno,)
        destinacije_ostrva = Destinacija.objects.filter(zemlja=zemlja_id, kategorija=ostrvo,)
        return render(request, 'destinacija/leto_zemlja.html', {
        'destinacije_kopno': destinacije_kopno,
        'destinacije_ostrva': destinacije_ostrva,
        'zemlja': zemlja
        })
