from django.urls import path
from destinacija.views import *

urlpatterns = [
    path('', PocetnaStranaView.as_view(), name='pocetna_strana'),

]
