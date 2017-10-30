from django.db import models

# Create your models here.
class Car(models.Model):
    car_position = models.IntegerField(verbose_name = 'Position Number')
    car_name = models.CharField(verbose_name = 'Car Name', max_length = 100)
    car_color = models.CharField(verbose_name = 'Car Color', max_length = 20)

    class Meta:
        ordering = ['car_position']