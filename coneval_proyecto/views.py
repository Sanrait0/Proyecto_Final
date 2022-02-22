from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "coneval_proyecto/index.html")

def carencias(request):
    return render(request, "coneval_proyecto/carencias.html")

def m_clasificacion(request):
    return render(request, "coneval_proyecto/m_clasificacion.html")

def pobreza(request):
    return render(request, "coneval_proyecto/prop_pobreza.html")