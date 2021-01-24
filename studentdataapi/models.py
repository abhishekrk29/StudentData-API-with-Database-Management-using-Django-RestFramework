from django.db import models

# Create your models here.
class Student(models.Model):
    firstname= models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    age= models.IntegerField()
    branch= models.CharField(max_length=50)
    city= models.CharField(max_length=50)

    def __str__(self):
        return self.firstname