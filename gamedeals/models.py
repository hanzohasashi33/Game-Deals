from django.db import models

# Create your models here.
class Developer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    description = models.CharField(max_length=500)
    role = models.CharField(max_length=200)
    picture = models.ImageField(upload_to ='uploads/')


    def __str__(self) -> str:
        return self.name
