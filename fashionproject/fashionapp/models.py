from django.db import models

# Create your models here.
class Fashion(models.Model):
    name=models.CharField(max_length=250)
    price=models.TextField()
    category=models.TextField()
    desc=models.TextField()
    img=models.ImageField(upload_to='photos')

    def __str__(self):
        return self.name
