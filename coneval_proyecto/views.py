import csv

from django.http import HttpResponse
from django.shortcuts import render
from coneval_proyecto.models import *

# Create your views here.
def index(request):
    return render(request, "coneval_proyecto/index.html")

def carencias(request):
    return render(request, "coneval_proyecto/carencias.html")

def m_clasificacion(request):
    return render(request, "coneval_proyecto/m_clasificacion.html")

def pobreza(request):
    return render(request, "admin")

def import_csv(request):
    COUNTIES = []
    with open("pobreza_2015.csv","r") as csv_file:
        data = list(csv.reader(csv_file,delimiter = ","))
        for row in data[1:]:
            COUNTIES.append(
                ConevalProyectoModel(
                    state=row[0],
                    county=row[1],
                    pct_pob=row[2]
                )
            )
    if len(COUNTIES)>0:
        ConevalProyectoModel.objects.bulk_create(COUNTIES)
    return HttpResponse("Carga completada")
