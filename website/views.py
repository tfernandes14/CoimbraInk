from django.shortcuts import render
from .models import *


def home(request):
    todas = get_lat_long()
    return render(request, 'base.html', {'lista': todas})


def get_lat_long():
    res = []
    tam_reprografias = len(list(Reprografia.objects.all()))
    for i in range(1, tam_reprografias + 1):
        rep = Reprografia.objects.get(id=i)
        aux = [rep.nome, rep.latitude, rep.longitude]
        res.append(aux)
    return res
