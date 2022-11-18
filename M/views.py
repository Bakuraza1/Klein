from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
import datetime
from collections import OrderedDict
from django.urls import reverse

# Create your views here.

number = 3

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
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    return render(request, "EG1.html",{'number': range(0,number), 'n': number})

def EG2(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    return render(request, "EG2.html",{'number': range(0,number), 'n': number})

def EG3(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    return render(request, "EG3.html",{'number': range(0,number), 'n': number})

def LUS(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    return render(request, "LUS.html",{'number': range(0,number), 'n': number})

def LUP(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    return render(request, "LUP.html",{'number': range(0,number), 'n': number})

def Cr(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    return render(request, "Cr.html",{'number': range(0,number), 'n': number})

def DO(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    return render(request, "DO.html",{'number': range(0,number), 'n': number})

def CH(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    return render(request, "CH.html",{'number': range(0,number), 'n': number})

def IT(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    return render(request, "IT.html",{'number': range(0,number), 'n': number})

def Va(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    return render(request, "Va.html",{'number': range(0,number), 'n': number})

def NDD(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    return render(request, "NDD.html",{'number': range(0,number), 'n': number})

def LA(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    return render(request, "LA.html",{'number': range(0,number), 'n': number})

def SP(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    return render(request, "sp.html",{'number': range(0,number), 'n': number})