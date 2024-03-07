from django.db import models

# Create your models here.


class Sample(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    image = models.ImageField()
    githublink = models.URLField(null=False,default='#')
    
    
    def __str__(self) -> str:
        return self.title
