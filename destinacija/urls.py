from django.urls import path
from destinacija.views import *

urlpatterns = [
    path('', PocetnaStranaView.as_view(), name='pocetna_strana'),
    path('Opšti_Uslovi_Putovanja/', UsloviPutovanjaView.as_view(), name='opsti_uslovi_putovanja'),
    path('Turistički_Pojmovi/', TuristickiPojmoviView.as_view(), name='turisticki_pojmovi'),
    path('Putno_Osiguranje/', PutnoOsiguranjeView.as_view(), name='putno_osiguranje'),
    path('Avio_Karte/', AvioKarteView.as_view(), name='avio_karte'),
    path('O_Nama/', ONamaView.as_view(), name='o_nama'),
    path('Kontakt/', KontaktView.as_view(), name='kontakt'),
]
