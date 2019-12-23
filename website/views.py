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
    todas = get_lat_long()
    tese = Tese.objects.all()
    a5 = Acinco.objects.all()
    a4 = Aquatro.objects.all()
    a3 = Atres.objects.all()
    a2 = Adois.objects.all()
    a1 = Aum.objects.all()
    a0 = Azero.objects.all()

    return render(request, 'simulador.html', {'reprografias': reprografias,
                                              'A5': a5, 'A4': a4, 'A3': a3,
                                              'A2': a2,'A1': a1, 'A0': a0, 'tese' : tese, 'lista': todas})


def contas(frente_verso, cores, frente, preto, encadernar, digitalizacao, plastificada, numero_paginas, objeto):
    # O objeto corresponde ao objeto certo que passamos, pode ser um do A5 ou um do A4

    conta = 0

    if frente_verso and cores:
        conta += objeto.frente_verso_cor_preco * numero_paginas
    elif frente_verso and preto:
        conta += objeto.frente_verso_preto_branco_preco * numero_paginas
    elif frente and cores :
        conta += objeto.frente_cor_preco * numero_paginas
    elif frente and preto:
        conta += objeto.frente_preto_branco_preco * numero_paginas

    if encadernar:
        conta += objeto.encadernacao
    if digitalizacao:
        conta += objeto.digitalizacao
    if plastificada:
        conta += objeto.plastificacao

    return conta