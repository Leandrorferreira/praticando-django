from django.db import models

# Create your models here.
class Role(models.Model):
    titulo = models.CharField(max_length=100, null = False, blank = False)
    local = models.CharField(max_length=100, null = False, blank = False)

    def __str__(self):
        return self.titulo