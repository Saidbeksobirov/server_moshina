from django.db import models

# Create your models here.


class CarModel(models.Model):
    objects = None
    image = models.ImageField(upload_to='media')
    name = models.CharField(max_length=155)
    info = models.TextField(null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name