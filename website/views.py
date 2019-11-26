from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import *


def home(request):
    todas = get_lat_long()
    print(todas)
    return render(request, 'base.html', {'lista': todas})


def get_lat_long():
    res = []
    tam_reprografias = len(list(Reprografia.objects.all()))
    print("&&&&", tam_reprografias)
    for i in range(1, tam_reprografias + 2):
        try:
            rep = Reprografia.objects.get(id=i)
        except ObjectDoesNotExist:
            rep = None
        if rep is not None:
            aux = [rep.nome, rep.latitude, rep.longitude]
            res.append(aux)
    return res
