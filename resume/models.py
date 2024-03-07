from django.db import models

# Create your models here.


class Education(models.Model):
    UniName = models.CharField(max_length=40)
    year = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.UniName 


class Experience(models.Model):
    title = models.CharField(max_length=40)
    year = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.title


class Skills(models.Model):
    title = models.CharField(max_length=40)
    level = models.IntegerField()

    def __str__(self) -> str:
        return self.title 
    
    