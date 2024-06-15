from django.shortcuts import render
from .forms import Informacion_form
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.apps import apps
from reportlab.pdfgen import canvas
from .models import Informacion_model




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



def inicio_view(request):
    
    news = Informacion_model.objects.all()

    if request.method == 'POST':
        form = Informacion_form(request.POST)
        if form.is_valid():
            campo1 = form.cleaned_data['campo1']
            campo2 = form.cleaned_data['campo2']
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="informacion.pdf"'
            
            # Crear un lienzo para el PDF usando ReportLab
            p = canvas.Canvas(response)
            
            # Agregar texto al PDF
            p.drawString(100, 800, f'Campo 1: {campo1}')
            p.drawString(100, 780, f'Campo 2: {campo2}')
            
            # Finalizar la página del PDF
            p.showPage()
            
            # Guardar y cerrar el documento PDF
            p.save()
            
            # Devolver la respuesta HTTP con el PDF generado
            return response
    else:
        form = Informacion_form()

    context = {'form':form, 'news': news}
    return render(request, 'Inicio.html', context)