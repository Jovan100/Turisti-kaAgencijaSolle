from django.urls import path
from destinacija.views import *

urlpatterns = [
    path('', PocetnaStranaView.as_view(), name='pocetna_strana'),
    path('Opšti_Uslovi_Putovanja/', UsloviPutovanjaView.as_view(), name='opsti_uslovi_putovanja'),
    path('Turistički_Pojmovi/', TuristickiPojmoviView.as_view(), name='turisticki_pojmovi'),
]
