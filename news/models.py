from django.db import models

class Informacion_model(models.Model):
    
    campo1 = models.CharField(max_length=100)
    campo2 = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to="Img-model/", blank=True)
    
    
    def __str__(self) -> str:
        return f'Pensamiento #{self.id}'