from django.db import models

# Create your models here.
class NewCar(models.Model):
    carname = models.CharField(max_length = 70)
    cardesc = models.CharField(max_length = 255)
    carimage = models.ImageField(upload_to = "newcarimage")


    def __str__(self):
        return self.carname