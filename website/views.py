from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import *
import requests


def home(request):
    reprografias = Reprografia.objects.all()
    todas = get_lat_long()
    print(todas)
    return render(request, 'base.html', {'reprografias': reprografias, 'lista': todas})


def get_lat_long():
    res = []
    tam_reprografias = len(list(Reprografia.objects.all()))
    response = requests.post('https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyCrc4kHDhi7GOYb5IBKUn1mrj6MsX85eNg')
    res.append(["", response.json()['location']['lat'], response.json()['location']['lng']])
    for i in range(1, tam_reprografias + 2):
        try:
            rep = Reprografia.objects.get(id=i)
        except ObjectDoesNotExist:
            rep = None
        if rep is not None:
            aux = [rep.nome, rep.latitude, rep.longitude]
            res.append(aux)
    return res


def simulador(request):
    reprografias = Reprografia.objects.all()

    a5 = Acinco.objects.all()
    tese = Tese.objects.all()
    a4 = Aquatro.objects.all()
    a3 = Atres.objects.all()
    a2 = Adois.objects.all()
    a1 = Aum.objects.all()
    a0 = Azero.objects.all()

    return render(request, 'simulador.html', {'reprografias': reprografias,
                                              'A5': a5, 'A4': a4, 'A3': a3,
                                              'A2': a2, 'A1': a1, 'A0': a0, 'tese': tese})
