from django.shortcuts import render
from .forms import Informacion_form
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.apps import apps
from reportlab.pdfgen import canvas
from .models import Informacion_model
from asgiref.sync import sync_to_async
import time





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

import asyncio
def inicio_view(request):
    
    """ def func_async(mensagge):
        return mensagge
      
    async_function = sync_to_async(func_async, thread_sensitive=True)
    
    async def main():
        # Usa await para obtener el resultado de la función asíncrona
        resultado = await async_function("Tecnologías:")
        return resultado

    resultado = asyncio.run(main()) """
    
    news = Informacion_model.objects.all()
 

    if request.method == 'POST':
        form = Informacion_form(request.POST)
        if form.is_valid():
            campo1 = form.cleaned_data['campo1']
            campo2 = form.cleaned_data['campo2']
            
   

    context = { 'news': news, }
    return render(request, 'Inicio.html', context,  )