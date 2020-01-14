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
