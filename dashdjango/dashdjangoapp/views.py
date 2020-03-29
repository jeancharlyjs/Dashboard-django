from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
# Create your views here.

class index(View):
    def get(self, request, *args, **kwargs):
        context = {
            "Tesla" : "Nikola Tesla - Genio por Excelencia"
        }
        return render(request, "index.html", context)

def dashboard(request):
    cientificos = ['Nikola Tesla', 'Issac Newton', 'Nicolas Copernico', 'Maria Curie', 'Arquimedes', 'Erwin Schrödinger']
    puntos = [50, 19, 3, 5, 2, 3]
    datos = {
            "labels": puntos,
            "cientificos": cientificos
    }
    return JsonResponse(datos)
