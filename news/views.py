from django.shortcuts import render, redirect
from .forms import Informacion_form
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.apps import apps
from reportlab.pdfgen import canvas
from .models import Informacion_model
from asgiref.sync import sync_to_async
import asyncio
from django.views import View



def inicio_view(request):

    news = Informacion_model.objects.all()     
    context = { 'news': news,}
    return render(request, 'Inicio.html', context)



class Contact_view(View):
    
    def get(self, request):
        form = Informacion_form()
        return render(request, 'test.html', {'form': form, 'message': 'Operación asíncrona completada'})
    
    def post(self, request):
        form = Informacion_form(request.POST)
        
        if form.is_valid():
            self.guardar_formulario(form)
            return redirect('inicio_view')
        
        return render(request, 'test.html', {'form': form, 'message': 'Operación asíncrona fallida'})
    
    def guardar_formulario(self, form):
        form.save()
        
        
        

def models_view(request):
    Info_model = Informacion_model.objects.all()
    data = serializers.serialize('json', Info_model) 

    all_models = []
    installed_apps = apps.get_app_configs()

    for app_config in installed_apps:
        models = app_config.get_models()
        for model in models:
            all_models.append(model.__name__)


    return JsonResponse({'models': all_models})