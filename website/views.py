from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import *
import requests
from django.http import HttpResponseRedirect
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse
import json

def home(request):
    

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


def simulador(request,pk):
    reprografia = Reprografia.objects.get(pk=pk)
    a5_res = Acinco.objects.get(reprografia=reprografia)
    a4_res = Aquatro.objects.get(reprografia=reprografia)
    a3_res = Atres.objects.get(reprografia=reprografia)
    a2_res = Adois.objects.get(reprografia=reprografia)
    a1_res = Aum.objects.get(reprografia=reprografia)
    a0_res = Azero.objects.get(reprografia=reprografia)
    
    resultado_5 = a5_res.serialize()
    resultado_4 = a4_res.serialize()
    resultado_3 = a3_res.serialize()
    resultado_2 = a2_res.serialize()
    resultado_1 = a1_res.serialize()
    resultado_0 = a0_res.serialize()

    resultado = [resultado_5, resultado_4, resultado_3, resultado_2, resultado_1, resultado_0]
    
    return JsonResponse(resultado, safe=False)


def busca_pagina(request,pk,choice):
    reprografia = Reprografia.objects.get(pk=pk)

    
    if(choice=="Azero"):
        objeto = Azero.objects.get(reprografia=reprografia).serialize()
    elif(choice=="Aum"):
        objeto = Aum.objects.get(reprografia=reprografia).serialize()
    elif(choice=="Adois"):
        objeto = Adois.objects.get(reprografia=reprografia).serialize()
    elif(choice=="Atres"):
        objeto = Atres.objects.get(reprografia=reprografia).serialize()
    elif(choice=="Aquatro"):
        objeto = Aquatro.objects.get(reprografia=reprografia).serialize()
    elif(choice=="Acinco"):
        objeto = Acinco.objects.get(reprografia=reprografia).serialize()
    
    return JsonResponse(objeto, safe=False)


    
                    



def get_lat_long():
    res = []
    tam_reprografias = len(list(Reprografia.objects.all()))
    res.append(["", 40.2040891, -8.4125606])
    for i in range(1, tam_reprografias + 2):
        try:
            rep = Reprografia.objects.get(id=i)
        except ObjectDoesNotExist:
            rep = None
        if rep is not None:
            aux = [rep.nome, rep.latitude, rep.longitude]
            res.append(aux)
    return res



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