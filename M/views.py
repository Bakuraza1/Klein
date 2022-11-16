from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
import datetime
from collections import OrderedDict
from django.urls import reverse

# Create your views here.

def test(request):
    return render(request, "nav.html")

def gtest(request):
    return render(request, "gtest.html")

def welcome(request):
    return render(request, "welcome.html")

def metodos(request):
    return render(request, "metodos.html")

def graficador(request):
    if request.method == 'POST':
        return render(request, "graficador.html", {'fun':[request.POST["funcion"]]})
    return render(request, "graficador.html", {'fun':['x^2']})

def ayuda(request):
    return render(request, "ayuda.html")

def BI(request):
    return render(request, "BI.html")

def B(request):
    return render(request, "B.html")

def PF(request):
    return render(request, "PF.html")

def PFi(request):
    return render(request, "PFi.html")

def NR(request):
    return render(request, "NR.html")

def SEC(request):
    return render(request, "SEC.html")

def RM(request):
    return render(request, "RM.html")

def EG1(request):
    return render(request, "EG1.html")

def EG2(request):
    return render(request, "EG2.html")

def EG3(request):
    return render(request, "EG3.html")

def LUS(request):
    return render(request, "LUS.html")

def LUP(request):
    return render(request, "LUP.html")

def Cr(request):
    return render(request, "Cr.html")

def DO(request):
    return render(request, "DO.html")

def CH(request):
    return render(request, "CH.html")

def IT(request):
    return render(request, "IT.html")

def Va(request):
    return render(request, "Va.html")

def NDD(request):
    return render(request, "NDD.html")

def LA(request):
    return render(request, "LA.html")

def SP(request):
    return render(request, "sp.html")