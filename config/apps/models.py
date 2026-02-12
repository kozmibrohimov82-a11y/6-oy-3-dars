from django.db import models

# Create your models here.


class Brand(models.Model):
    name=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.name
    

class Car(models.Model):
    name=models.CharField(max_length=200)
    content=models.TextField(blank=True,null=True)
    price=models.DecimalField(max_digits=20,decimal_places=2)
    color=models.CharField(max_length=20)
    image=models.ImageField(upload_to="image/",blank=True,null=True)
    video=models.FileField(upload_to='video/',blank=True,null=True)
    marka=models.CharField(max_length=150)
    year=models.DecimalField(max_digits=4,decimal_places=0)
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)

    def __str__(self):
        return self.name








