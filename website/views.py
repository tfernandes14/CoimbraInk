from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from .models import *


from .models import *


def home(request):
    reprografias = Reprografia.objects.all()
    todas = get_lat_long()
    print(todas)
    return render(request, 'base.html', {'reprografias': reprografias, 'lista': todas})


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


def simulador(request):
    reprografias = Reprografia.objects.all()
    todas = get_lat_long()
    A5 = Acinco.objects.all()
    tese = Tese.objects.all()
    A4 = Aquatro.objects.all()
    A3 = Atres.objects.all()
    A2 = Adois.objects.all()
    A1 = Aum.objects.all()
    A0 = Azero.objects.all()

    return render(request, 'simulador.html', {'reprografias': reprografias,
                                              'A5': A5, 'A4': A4, 'A3': A3,
                                              'A2': A2,'A1': A1, 'A0': A0, 'tese' : tese, 'lista': todas})


def contas(frente_verso,cores,frente,preto,encadernar,digitalizacao,plastificada,numerosdePaginas,objeto):
    #o objeto corresponde ao objeto certo que passamos, pode ser um do A5 ou um do A4

    conta=0

    if(frente_verso and cores):
        conta+=(objeto.frente_verso_cor_preco*numerosdePaginas)
    elif(frente_verso and preto):
        conta+=(objeto.frente_verso_preto_branco_preco*numerosdePaginas)
    elif(frente and cores):
        conta+=(objeto.frente_cor_preco*numerosdePaginas)
    elif(frente and preto):
        conta+=(objeto.frente_preto_branco_preco*numerosdePaginas)

    if(encadernar):
        conta+=objeto.encadernacao
    if(digitalizacao):
        conta+=objeto.digitalizacao
    if(plastificada):
        conta+=objeto.plastificacao

    return conta