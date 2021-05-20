from django.db import models

# Create your models here.
class Banner(models.Model):
    text = models.CharField(max_length=500)
    height = models.IntegerField()
    width = models.IntegerField(default=0)
    background_color = models.CharField(max_length=50)
    font_color = models.CharField(max_length=50)
    
    def __str__(self):
        return f'{self.text}'
        
    