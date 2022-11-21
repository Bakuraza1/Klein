from django.shortcuts import render
from .metodos import *
# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
import datetime
from collections import OrderedDict
from django.urls import reverse
import numpy as np

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
    if request.method == 'POST':
        res = [[1,0.5,1],[2,1.5,2]]
        f = lambda x: eval(request.POST["funcion"])
        x0 = float(request.POST["Valor-i"])
        dx = float(request.POST["delta"])
        n = int(request.POST["niter"])
        arg = [str(request.POST["funcion"]), x0,dx,n]
        res = (incremental_search(f, x0, dx, n))
        return render(request, "BI.html", {"res": res, "arg" : arg})
    return render(request, "BI.html", {"flag": True})

def B(request):
    if request.method == 'POST':
        f = (request.POST["funcion"])
        a = float(request.POST["a"])
        b = float(request.POST["b"])
        tol = float(request.POST["tol"])
        niter = int(request.POST["niter"])
        arg = [str(request.POST["funcion"]), a,b,tol, niter]
        res = (biseccion(f, a, b, tol, niter))
        return render(request, "B.html", {"res": res[0], "arg" : arg,'final':res[1] })
    return render(request, "B.html", {"flag": True})

def PF(request):
    if request.method == 'POST':
        f = (request.POST["funcion"])
        a = float(request.POST["a"])
        b = float(request.POST["b"])
        tol = float(request.POST["tol"])
        niter = int(request.POST["niter"])
        arg = [str(request.POST["funcion"]), a,b,tol, niter]
        res = (regla_falsa(f, 1, a, b, tol, niter))
        return render(request, "PF.html", {"res": res[0], "arg" : arg, 'final':res[1]})
    return render(request, "PF.html")

def PFi(request):
    if request.method == 'POST':
        f = (request.POST["funcionf"])
        g = (request.POST["funciong"])
        x0 = float(request.POST["x0"])
        tol = float(request.POST["tol"])
        niter = int(request.POST["niter"])
        arg = [f, g, x0,tol, niter]
        res = (punto_fijo(f, g, x0, tol, niter))
        print(res)
        return render(request, "PFi.html", {"res": res[0], "arg" : arg, 'final': res[1]})
    return render(request, "PFi.html")

def NR(request):
    if request.method == 'POST':
        f = (request.POST["funcion"])
        g = (request.POST["funcionf"])
        x0 = float(request.POST["x0"])
        tol = float(request.POST["tol"])
        niter = int(request.POST["niter"])
        arg = [f, g, x0,tol, niter]
        res = (newton_raphson(f, g, x0, tol, niter))
        print(res)
        return render(request, "NR.html", {"res": res[0], "arg" : arg, 'final': res[1]})
    return render(request, "NR.html")

def SEC(request):
    if request.method == 'POST':
        f = (request.POST["funcion"])
        x0 = float(request.POST["x0"])
        x1 = float(request.POST["x1"])
        tol = float(request.POST["tol"])
        niter = int(request.POST["niter"])
        arg = [x0,x1, f,tol, niter]
        res = (secante(x0, x1, f, tol, niter))
        print(res)
        return render(request, "SEC.html", {"res": res[0], "arg" : arg, 'final':res[1]})
    return render(request, "SEC.html")

def RM(request):
    if request.method == 'POST':
        f = (request.POST["funcion"])
        df = (request.POST["funcionf"])
        df2 = (request.POST["funcionff"])
        x0 = float(request.POST["x0"])
        tol = float(request.POST["tol"])
        niter = int(request.POST["niter"])
        arg = [f, df,df2,x0, f,tol, niter]
        res = (multiple_roots(x0,f, df, df2, tol, niter))
        return render(request, "RM.html", {"res": res[0], "arg" : arg, 'final':res[1]})
    return render(request, "RM.html")

def EG1(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    if request.method=='POST' and (request.POST["submit"] == 'Completado'):
        matrix = []
        vector = []
        for i in range(0, number):
            vector.append(request.POST["v%(i)d" % {"i":i}])
            matrix.append([])
            for j in range(0,number):
                matrix[i].append(request.POST["m%(i)d%(j)d" % {"i":i,"j": j}])
        matrix = np.array(matrix).astype(np.float64)
        vector = np.array(vector).astype(np.float64)
        res = simple_gauss(matrix, vector)
        res2 = regressive_substitution(np.array(res[-1]))
        return render(request, "EG1.html",{'number': range(0,number), 'n': number, 'res':res, 'res2':res2})
    return render(request, "EG1.html",{'number': range(0,number), 'n': number})

def EG2(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    if request.method=='POST' and (request.POST["submit"] == 'Completado'):
        matrix = []
        vector = []
        for i in range(0, number):
            vector.append(request.POST["v%(i)d" % {"i":i}])
            matrix.append([])
            for j in range(0,number):
                matrix[i].append(request.POST["m%(i)d%(j)d" % {"i":i,"j": j}])
        matrix = np.array(matrix).astype(np.float64)
        vector = np.array(vector).astype(np.float64)
        res = gauss_partial_pivot(matrix, vector)
        res2 = regressive_substitution(np.array(res[-1]))
        return render(request, "EG2.html",{'number': range(0,number), 'n': number, 'res':res, 'res2':res2})
    return render(request, "EG2.html",{'number': range(0,number), 'n': number})

def EG3(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    if request.method=='POST' and (request.POST["submit"] == 'Completado'):
        matrix = []
        vector = []
        for i in range(0, number):
            vector.append(request.POST["v%(i)d" % {"i":i}])
            matrix.append([])
            for j in range(0,number):
                matrix[i].append(request.POST["m%(i)d%(j)d" % {"i":i,"j": j}])
        matrix = np.array(matrix).astype(np.float64)
        vector = np.array(vector).astype(np.float64)
        res = gauss_total_pivot(matrix, vector)
        res2 = regressive_substitution(np.array(res[0][-1]))
        ans = res[1]
        print(ans)
        for i in range(0, len(ans)):
            temp = res2[ans[i]]
            res2[ans[i]] = res2[i]
            res2[i] = temp
        return render(request, "EG3.html",{'number': range(0,number), 'n': number, 'res':res[0],'res1':res[1], 'res2':res2})
    return render(request, "EG3.html",{'number': range(0,number), 'n': number})

def LUS(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    if request.method=='POST' and (request.POST["submit"] == 'Completado'):
        matrix = []
        vector = []
        for i in range(0, number):
            vector.append(request.POST["v%(i)d" % {"i":i}])
            matrix.append([])
            for j in range(0,number):
                matrix[i].append(request.POST["m%(i)d%(j)d" % {"i":i,"j": j}])
        matrix = np.array(matrix).astype(np.float64)
        vector = np.array(vector).astype(np.float64)
        res = lu_gauss(matrix, vector)
        for i in res[0]:
            print(i)
        return render(request, "LUS.html",{'number': range(0,number), 'n': number, 'res':res[0], 'res2':res[1], 'names': ['z','U','L','M']})
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
    if request.method=='POST' and (request.POST["submit"] == 'Completado'):
        matrix = []
        vector = []
        for i in range(0, number):
            vector.append(request.POST["v%(i)d" % {"i":i}])
            matrix.append([])
            for j in range(0,number):
                matrix[i].append(request.POST["m%(i)d%(j)d" % {"i":i,"j": j}])
        matrix = np.array(matrix).astype(np.float64)
        vector = np.array(vector).astype(np.float64)
        res = crout(matrix, vector)
        for i in res[0]:
            print(i)
        return render(request, "Cr.html",{'number': range(0,number), 'n': number, 'res':res[0], 'res2':res[1], 'names': ['z','U','L']})
    return render(request, "Cr.html",{'number': range(0,number), 'n': number})

def DO(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    if request.method=='POST' and (request.POST["submit"] == 'Completado'):
        matrix = []
        vector = []
        for i in range(0, number):
            vector.append(request.POST["v%(i)d" % {"i":i}])
            matrix.append([])
            for j in range(0,number):
                matrix[i].append(request.POST["m%(i)d%(j)d" % {"i":i,"j": j}])
        matrix = np.array(matrix).astype(np.float64)
        vector = np.array(vector).astype(np.float64)
        res = dolittle_fac(matrix, vector)
        for i in res[0]:
            print(i)
        return render(request, "DO.html",{'number': range(0,number), 'n': number, 'res':res[0], 'res2':res[1], 'names': ['z','U','L']})
    return render(request, "DO.html",{'number': range(0,number), 'n': number})

def CH(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    if request.method=='POST' and (request.POST["submit"] == 'Completado'):
        matrix = []
        vector = []
        for i in range(0, number):
            vector.append(request.POST["v%(i)d" % {"i":i}])
            matrix.append([])
            for j in range(0,number):
                matrix[i].append(request.POST["m%(i)d%(j)d" % {"i":i,"j": j}])
        matrix = np.array(matrix).astype(np.float64)
        vector = np.array(vector).astype(np.float64)
        res = cholesky_factorization(matrix, vector)
        for i in res[0]:
            print(i)
        return render(request, "CH.html",{'number': range(0,number), 'n': number, 'res':res[0], 'res2':res[1], 'names': ['z','U','L']})
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
    if request.method=='POST' and (request.POST["submit"] == 'Completado'):
        x = []
        y = []
        for i in range(0, number):
            x.append(request.POST["x%(i)d" % {"i":i}])
            y.append(request.POST["y%(i)d" % {"i":i}])
        x = np.array(x).astype(np.float64)
        y = np.array(y).astype(np.float64)
        res = vandermonde_method(x, y)
        c = range(0,len(res['coeficients']))[::-1]
        print(res['coeficients'])
        return render(request, "Va.html",{'number': range(0,number), 'n': number, 'res':res['matrix'].tolist(), 'res2':res['coeficients'], 'cof':c, 'y':y})
    return render(request, "Va.html",{'number': range(0,number), 'n': number})

def NDD(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    if request.method=='POST' and (request.POST["submit"] == 'Completado'):
        x = []
        y = []
        for i in range(0, number):
            x.append(request.POST["x%(i)d" % {"i":i}])
            y.append(request.POST["y%(i)d" % {"i":i}])
        x = np.array(x).astype(np.float64)
        y = np.array(y).astype(np.float64)
        res = newton_interpolacion(x, y)
        r = ""
        print(res['coef'])
        cont = 0
        for i in res['coef']:
            cont+=1
            if i > 0:
                r += '+' + str(i)
            else:
                r += str(i)
            for j in x[1:cont]:
                if (j*-1) > 0:
                    r += '(x+' + str(j*-1) +')'
                else:
                    r += '(x' + str(j*-1) +')'
        print(r)
        return render(request, "NDD.html",{'number': range(0,number), 'n': number, 'res':res['table'], 'res2':res['coef'], 'x':x.tolist(), 'na':len(res['table'][0]), 'r':r})
    return render(request, "NDD.html",{'number': range(0,number), 'n': number})

def LA(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    if request.method=='POST' and (request.POST["submit"] == 'Completado'):
        puntos = []
        for i in range(0, number):
            puntos.append([request.POST["x%(i)d" % {"i":i}], (request.POST["y%(i)d" % {"i":i}])])
        puntos = np.array(puntos).astype(np.float64)
        res = lagrange(puntos)
        print((res[0]))
        return render(request, "LA.html",{'number': range(0,number), 'n': number, 'res':res[0], 'ans':res[1]})
    return render(request, "LA.html",{'number': range(0,number), 'n': number})

def SP(request):
    global number
    if request.method=='POST' and (request.POST["submit"] == 'Actualizar'):
        number = int(request.POST["number"])
    if request.method=='POST' and (request.POST["submit"] == 'Completado'):
        x = []
        y = []
        metodo = int(request.POST['metodo'])
        for i in range(0, number):
            x.append(request.POST["x%(i)d" % {"i":i}])
            y.append(request.POST["y%(i)d" % {"i":i}])
        x = np.array(x).astype(np.float64)
        y = np.array(y).astype(np.float64)
        res = spline(x, y, metodo)
        ans = []
        
        for i in res:
            stra = ""
            for j in range(0 , len(i)):
                if j > 0:
                    if (j+1) == len(i):
                        stra += '+' +  str(i[j])
                    else:
                        stra += '+' + str(i[j]) + 'x{}'.format(get_super(str(len(i)-j-1)))
                else:  
                    if (j+1) == len(i):
                        stra +=  str(i[j])
                    else:
                        stra +=  str(i[j]) + 'x{}'.format(get_super(str(len(i)-j-1)))
            ans.append(stra)
        print(ans)
                
        print(res)
        return render(request, "sp.html",{'number': range(0,number), 'n': number, 'res':res, 'ans':ans})
    return render(request, "sp.html",{'number': range(0,number), 'n': number})


def get_super(x):
    normal = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+-=()"
    super_s = "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾQᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰᶦʲᵏˡᵐⁿᵒᵖ۹ʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁼⁽⁾"
    res = x.maketrans(''.join(normal), ''.join(super_s))
    return x.translate(res)