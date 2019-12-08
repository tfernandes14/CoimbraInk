from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages

from .models import *


def home(request):
    return render(request, 'base.html')

def simulador(request):
    reprografias = Reprografia.objects.all()

    A5 = Acinco.objects.all()
    tese = Tese.objects.all()
    A4 = Aquatro.objects.all()
    A3 = Atres.objects.all()
    A2 = Adois.objects.all()
    A1 = Aum.objects.all()
    A0 = Azero.objects.all()

    return render(request, 'simulador.html', {'reprografias': reprografias,
                                              'A5': A5, 'A4': A4, 'A3': A3,
                                              'A2': A2,'A1': A1, 'A0': A0, 'tese' : tese})