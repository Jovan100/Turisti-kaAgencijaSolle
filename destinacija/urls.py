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
    path('Grčka/', GrckaListView.as_view(), name='grcka'),
    path('Grčka/Kopno/', GrckaKopnoView.as_view(), name='grcka_kopno'),
    path('Grčka/Ostrva/', GrckaOstrvaView.as_view(), name='grcka_ostrva'),
    path('Leto/', LetoView.as_view(), name='leto'),
    path('Leto/<str:zemlja>/', LetoZemljaView.as_view(), name='leto_zemlja'),
    path('<str:naziv_destinacije>/', DestinacijaView.as_view(), name='destinacija'),
]
