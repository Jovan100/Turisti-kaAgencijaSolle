from django.views.generic import DetailView, ListView
from django.views.generic.base import TemplateView
from django.shortcuts import render
from destinacija.models import (
    Agencija,
    Cenovnik,
    Destinacija,
    KategorijaDestinacije,
    Zemlja
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
